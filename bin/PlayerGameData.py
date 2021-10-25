class RawPGD:
    # Initial Data
    summoner_name = None
    match = None
    pifl = None

    # Raw Game Data
    deaths = None
    kills = None
    assists = None
    game_time = None
    cs = None
    lost = None
    champ_name = None
    early_surrender = None
    surrender = None
    role = None
    wards_bought = None
    kp = None
    possibly_inted = None

    # Processed Raw
    cspm = None
    teammates_int = None
    player_int = None

    def __init__(self, match, summoner_name):
        self.summoner_name = summoner_name
        self.match = match
        self.pifl = self.match["info"]["participants"]
        self.init_raw()
        self.process_raw()

    def init_raw(self):  # TODO
        for i in range(len(self.pifl)):
            if self.pifl[i]["summonerName"] == self.summoner_name:
                tmp = self.pifl[i]
                # Data from info dictionary
                self.game_time = self.match["info"]["gameDuration"] / 60

                # Data from participants dictionary
                self.deaths = tmp["deaths"]
                self.kills = tmp["kills"]
                self.champ_name = tmp["championName"]
                self.early_surrender = tmp["teamEarlySurrendered"]
                self.assists = self.pifl[i]["assists"]
                self.cs = self.pifl[i]["totalMinionsKilled"]
                self.role = self.pifl[i]["teamPosition"]

    def process_raw(self):  # TODO
        for i in range(len(self.pifl)):
            if self.pifl[i]["summonerName"] == self.summoner_name:
                self.cspm = self.cs / self.game_time
                if self.pifl[i]["win"]:
                    self.lost = False
                else:
                    self.lost = True

                if self.deaths > 0:
                    if (self.kills / self.deaths) <= .1 and self.role != "SUPPORT":
                        self.possibly_inted = True
                    else:
                        self.possibly_inted = False

    def __str__(self):
        return str(self.kills) + " " + str(self.deaths) + " " + str(self.game_time) + " " + str(self.cs) + " " \
               + str(self.lost) + " " + str(self.champ_name) + " " + str(self.early_surrender) + " " + str(self.role)


class AggPGD:  # TODO
    # Initial Data
    raw_pgd_list = None
    summoner_name = None

    # Aggregated Data
    curr_lss_stk = None
    lrgst_lss_stk = None
    wl_ratio = None
    avg_kp = None
    avg_kills = 0
    avg_KD = 0
    avg_deaths = 0
    avg_int = 0
    losses = 0
    avg_cs = 0

    def __init__(self, summoner_name, raw_pgd_list):
        self.raw_pgd_list = raw_pgd_list
        self.summoner_name = summoner_name
        self.init_data()

    def init_data(self):
        for i in range(len(self.raw_pgd_list)):
            self.avg_deaths += self.raw_pgd_list[i].deaths
        self.avg_deaths /= len(self.raw_pgd_list)

        for i in range(len(self.raw_pgd_list)):
            self.avg_kills += self.raw_pgd_list[i].kills
        self.avg_kills /= len(self.raw_pgd_list)
        if self.avg_deaths > 0:
            self.avg_KD = self.avg_kills / self.avg_deaths
        else:
            self.avg_KD = self.avg_kills

        for i in range(len(self.raw_pgd_list)):
            self.avg_cs += self.raw_pgd_list[i].cs
        self.avg_cs /= len(self.raw_pgd_list)

        for i in range(len(self.raw_pgd_list)):
            if self.raw_pgd_list[i].possibly_inted:
                self.avg_int += 1
        self.avg_int /= len(self.raw_pgd_list)

        # TODO - Not sure if losses is actually working
        for i in range(len(self.raw_pgd_list)):
            if self.raw_pgd_list[i].lost:
                self.losses += 1

        self.wl_ratio = 1 - (self.losses / len(self.raw_pgd_list))
