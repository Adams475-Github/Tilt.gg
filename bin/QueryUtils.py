import datetime

import requests

from bin import MiscUtils
from riotwatcher import LolWatcher


class QueryUtils:
    api_key = 'RGAPI-bb5822f6-753b-4bbb-8586-359614ec5837'
    watcher = LolWatcher(api_key)
    default_region = ""

    def __init__(self, default_region):
        self.default_region = default_region

    # Returns X recent matches, with each match being 5 hours within the last one
    def query_recent_games(self, summoner_name, amount):
        summoner = self.watcher.summoner.by_name(self.default_region, summoner_name)
        summoner_id = summoner["puuid"]

        raw_recent_matches = self.watcher.match.matchlist_by_puuid(region='AMERICAS', puuid=summoner_id, count=amount)
        match_dates = []
        recent_matches = []

        for i in range(len(raw_recent_matches)):
            match = self.watcher.match.by_id(region='AMERICAS', match_id=raw_recent_matches[i])
            mtime = match["info"]["gameStartTimestamp"]
            formatted_time = datetime.datetime.utcfromtimestamp(mtime / 1000).strftime('%Y-%m-%d %H:%M:%S')
            hour = int(formatted_time[12:13])
            if i > 0:
                if not MiscUtils.is_recent(formatted_time, match_dates[i - 1]):
                    break
            match_dates.append(formatted_time)
            recent_matches.append(match)
        return recent_matches

    def summoners_in_curr_game(self, summoner_name):
        participants_names = []
        summoner = self.watcher.summoner.by_name(self.default_region, summoner_name)
        summoner_id = summoner["id"]
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



