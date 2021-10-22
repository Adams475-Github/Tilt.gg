class RawPGD:
    # Initial Data
    summoner_name = None
    match = None

    # Raw Game Data
    deaths = None
    kills = None
    game_time = None
    cs = None
    win = None
    champ_name = None
    early_surrender = None
    surrender = None
    role = None
    wards_bought = None
    kp = None

    # Processed Raw
    cspm = None
    teammates_int = None
    player_int = None

    def __init__(self, match, summoner_name):
        self.summoner_name = summoner_name
        self.match = match
        self.init_raw()
        self.process_raw()

    def init_raw(self):  # TODO
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

    def process_raw(self):  # TODO
        return None

    def __str__(self):
        return str(self.kills) + " " + str(self.deaths) + " " + str(self.game_time) + " " + str(self.cs) + " " \
               + str(self.win) + " " + str(self.champ_name) + " " + str(self.early_surrender) + " " + str(self.role)


class AggPGD:  # TODO
    # Initial Data
    raw_pgd_list = None

    # Aggregated Data
    curr_lss_stk = None
    lrgst_lss_stk = None
    wl_ratio = None
    avg_kp = None

    def __init__(self, raw_pgd_list):
        self.raw_pgd_list = raw_pgd_list


