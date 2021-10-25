from riotwatcher import LolWatcher
import datetime
import requests
import Config
import PlayerGameData
import Constants


def get_live_game_agg_pgd_list(region, summoner_name):
    squ = SummonerQueryUtils(region, summoner_name)
    summoners_in_live_game = squ.get_summoners_in_live_game()  # Summoners In Current Game
    summoner_rg_pairs = {}
    for i in range(len(summoners_in_live_game)):
        temp_squ = SummonerQueryUtils(region, summoners_in_live_game[i])
        recent_games = temp_squ.get_recent_games()
        raw_pgd_list = []
        for j in range(len(recent_games)):
            raw_pgd_list.append(PlayerGameData.RawPGD(recent_games[j], summoners_in_live_game[i]))
        summoner_rg_pairs[summoners_in_live_game[i]] = raw_pgd_list

    agg_pgd_list = []
    for i in range(len(summoner_rg_pairs)):
        agg_pgd_list.append(PlayerGameData.AggPGD(summoners_in_live_game[i],
                                                  summoner_rg_pairs[summoners_in_live_game[i]]))
    return agg_pgd_list
#  Returns a list of AggPGDs


class SummonerQueryUtils:
    api_key = Config.api_key
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
    def get_recent_games(self):
        raw_recent_matches = self.watcher.match \
            .matchlist_by_puuid(region='AMERICAS', puuid=self.summoner_id, count=Constants.MAX_QUERY)
        match_dates = []
        recent_matches = []

        for i in range(len(raw_recent_matches)):
            match = self.watcher.match.by_id('AMERICAS', raw_recent_matches[i])
            mtime = match["info"]["gameStartTimestamp"]
            formatted_time = datetime.datetime.utcfromtimestamp(mtime / 1000).strftime('%Y-%m-%d %H:%M:%S')
            if i > 0:
                if not MiscUtils.is_recent(formatted_time, match_dates[i - 1]):
                    break
            else:
                if MiscUtils.not_today(formatted_time):
                    break
            match_dates.append(formatted_time)
            recent_matches.append(match)
        return recent_matches

    # Returns summoner names in the specified summoner's current game
    def get_summoners_in_live_game(self):
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

    def get_latest_match(self):
        match_id = self.watcher.match.matchlist_by_puuid(region='AMERICAS', puuid=self.summoner_id, count=1)
        return self.watcher.match.by_id(region='AMERICAS', match_id=match_id[0])


class MiscUtils:

    @staticmethod
    def not_today(time):
        today = datetime.date.today()
        d1 = int(today.strftime("%d"))
        d2 = int(time[8:10])
        if d1 != d2:
            return True
        return False

    @staticmethod
    def is_recent(time1, time2):
        m1 = int(time1[5:7])
        d1 = int(time1[8:10])
        h1 = int(time1[11:13])

        m2 = int(time2[5:7])
        d2 = int(time2[8:10])
        h2 = int(time2[11:13])

        if abs(h1 - h2) < 5:  # TODO (and I really mean TODO it is broken)
            if (m1 - m2) == 0:
                if (d1 - d2) == 0:
                    return True
        return False
