import datetime
import requests
from bin import MiscUtils, config
from riotwatcher import LolWatcher


class SummonerQueryUtils:
    api_key = config.api_key
    watcher = LolWatcher(api_key)
    default_region = ""
    summoner_name = None
    summoner = None

    def __init__(self, default_region, summoner_name):
        self.default_region = default_region
        self.summoner_name = summoner_name
        self.summoner = self.watcher.summoner.by_name(self.default_region, self.summoner_name)

    # Returns X recent matches, with each match being 5 hours within the last one
    def query_recent_games(self, amount):
        summoner_id = self.summoner["puuid"]
        raw_recent_matches = self.watcher.match.matchlist_by_puuid(region='AMERICAS', puuid=summoner_id, count=amount)
        match_dates = []
        recent_matches = []

        for i in range(len(raw_recent_matches)):
            match = self.watcher.match.by_id(region='AMERICAS', match_id=raw_recent_matches[i])
            mtime = match["info"]["gameStartTimestamp"]
            formatted_time = datetime.datetime.utcfromtimestamp(mtime / 1000).strftime('%Y-%m-%d %H:%M:%S')
            if i > 0:
                if not MiscUtils.is_recent(formatted_time, match_dates[i - 1]):
                    break
            match_dates.append(formatted_time)
            recent_matches.append(match)
        return recent_matches

    # Returns summoner names in the specified summoner's current game
    def summoners_in_curr_game(self):
        participants_names = []
        summoner_id = self.summoner["id"]
        curr_match = None
        try:
            curr_match = self.watcher.spectator.by_summoner(region='na1', encrypted_summoner_id=summoner_id)
        except requests.HTTPError as exception:
            print("Summoner not currently in a game!")
            return None
        participant_info_list = curr_match["participants"]
        for i in range(len(participant_info_list)):
            participant_info = participant_info_list[i]
            participants_names.append(participant_info["summonerName"])
        return participants_names





