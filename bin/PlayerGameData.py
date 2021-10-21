class PlayerGameData:
    deaths = None
    kills = None
    game_time = None
    possibly_inted = None
    kill_particip = None
    cs = None
    troll_build = None
    lost = None
    summoner_name = None
    match = None
    champ_name = None

    def __init__(self, match, summoner_name):
        self.summoner_name = summoner_name
        self.match = match
        self.init_data()

    def init_data(self):  # TODO
        participant_info_list = self.match["info"]["participants"]
        for i in range(len(participant_info_list)):
            if participant_info_list[i]["summonerName"] == self.summoner_name:
                self.deaths = participant_info_list[i]["deaths"]
                self.champ_name = participant_info_list[i]["champName"]

    def __str__(self):
        return "TODO"


