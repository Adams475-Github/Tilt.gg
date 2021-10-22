class PlayerGameData:
    match = None

    deaths = None
    kills = None
    game_time = None
    cs = None
    win = None
    champ_name = None
    early_surrender = None
    role = None
    item0 = None

    def __init__(self, match, summoner_name):
        self.summoner_name = summoner_name
        self.match = match
        self.init_data()

    def init_data(self):
        participant_info_list = self.match["info"]["participants"]
        for i in range(len(participant_info_list)):
            if participant_info_list[i]["summonerName"] == self.summoner_name:
                tmp = participant_info_list[i]
                self.deaths = tmp["deaths"]
                self.kills = tmp["kills"]
                self.champ_name = tmp["championName"]
                self.win = tmp["win"]
                self.early_surrender = tmp["teamEarlySurrendered"]
                self.role = tmp["lane"]
                self.cs = tmp["totalMinionsKilled"]
                self.item0 = tmp["item0"]

    def __str__(self):
        return str(self.kills) + " " + str(self.deaths) + " " + str(self.game_time) + " " + str(self.cs) + " " \
               + str(self.win) + " " + str(self.champ_name) + " " + str(self.early_surrender) + " " + str(self.role)
