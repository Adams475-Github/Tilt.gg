from riotwatcher import LolWatcher
import datetime
import requests
import config
import PlayerGameData
import Calculations


def get_agg_pd(region, summoner_name):
    squ = SummonerQueryUtils(region, summoner_name)
    sicg = squ.summoners_in_curr_game()  # Summoners In Current Game
    summoner_rg_pairs = {}
    for i in range(len(sicg)):
        temp_squ = SummonerQueryUtils(region, sicg[i])
        recent_games = temp_squ.recent_games(10)
        raw_pgd_list = []
        for j in range(len(recent_games)):
            raw_pgd_list.append(PlayerGameData.RawPGD(recent_games[j], sicg[i]))
        summoner_rg_pairs[sicg[i]] = raw_pgd_list

    agg_pgd_list = {}
    for i in range(len(summoner_rg_pairs)):
        agg_pgd_list[sicg[i]] = PlayerGameData.AggPGD(summoner_rg_pairs[sicg[i]])
    return agg_pgd_list


def tilt_agg(agg_pd_list):
    summoner_tilt_pairs = {}
    for i in range(len(agg_pd_list)):
        summoner_tilt_pairs[agg_pd_list[i]] = Calculations.calc_tilt(agg_pd_list)
    return summoner_tilt_pairs


class SummonerQueryUtils:
    api_key = config.api_key
    watcher = LolWatcher(api_key)
    default_region = ""
    summoner_name = None
    summoner = None
    summoner_id = None

    def __init__(self, default_region, summoner_name):
        self.default_region = default_region
        self.summoner_name = summoner_name
        self.summoner = self.watcher.summoner.by_name(self.default_region, self.summoner_name)
        self.summoner_id = self.summoner["puuid"]

    # Returns X recent matches, with each match being 5 hours within the last one
    def recent_games(self, amount):  # TODO remove amount
        raw_recent_matches = self.watcher.match.matchlist_by_puuid('AMERICAS', self.summoner_id, amount)
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
        summoner_id = self.summoner["id"]  # Different from normal puuid!
        try:
            curr_match = self.watcher.spectator.by_summoner(region='na1', encrypted_summoner_id=summoner_id)
        except requests.HTTPError:
            print("Summoner not currently in a game!")
            return None
        participant_info_list = curr_match["participants"]
        for i in range(len(participant_info_list)):
            participant_info = participant_info_list[i]
            participants_names.append(participant_info["summonerName"])
        return participants_names

    def latest_match(self):
        match_id = self.watcher.match.matchlist_by_puuid(region='AMERICAS', puuid=self.summoner_id, count=1)
        return self.watcher.match.by_id(region='AMERICAS', match_id=match_id[0])


class MiscUtils:

    @staticmethod
    def is_recent(time1, time2):
        m1 = int(time1[6:7])
        d1 = int(time1[9:10])
        h1 = int(time1[11:13])

        m2 = int(time2[6:7])
        d2 = int(time2[9:10])
        h2 = int(time2[11:13])

        if abs(h1 - h2) < 5:  # TODO (and I really mean TODO it is broken)
            if (m1 - m2) == 0:
                if (d1 - d2) == 0:
                    return True
        return False
