import SummonerQueryUtils
class PlayerGameData:
    deaths = None
    kills = None
    assists = None
    game_duration = None
    possibly_inted = None
    cs = None
    troll_build = None
    lost = None
    summoner_name = None
    match = None
    champ_name = None
    role = None

    def __init__(self, match, summoner_name):
        self.summoner_name = summoner_name
        self.match = match
        self.init_data()

    def init_data(self):  # TODO
        participant_info_list = self.match["info"]["participants"]
        for i in range(len(participant_info_list)):
            if participant_info_list[i]["summonerName"] == self.summoner_name:
                #Data from info dictionary
                self.game_duration = self.match["info"]["gameDuration"] / 60

                #Data from participants dictionary
                self.kills = participant_info_list[i]["kills"]
                self.deaths = participant_info_list[i]["deaths"]
                self.assists = participant_info_list[i]["assists"]
                self.champ_name = participant_info_list[i]["championName"]
                self.cs = participant_info_list[i]["totalMinionsKilled"] / self.game_duration
                self.role = participant_info_list[i]["teamPosition"]
                if participant_info_list[i]["win"] == True:
                    self.lost = False
                elif participant_info_list[i]["win"] == False:
                    self.lost = True
                
                if self.kills / self.deaths <= .1 and self.role != "SUPPORT":
                    self.possibly_inted == True
                else:
                    self.possibly_inted == False

             
            
    def __str__(self):
        return "TODO"


