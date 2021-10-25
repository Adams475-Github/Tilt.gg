class PlayerTiltProfile:
    tilt_value = None
    summoner_name = None
    puuid = None
    agg_pgd = None
    raw_pgd_list = None

    def __init__(self, summoner_name, tilt_value, agg_pgd):
        self.summoner_name = summoner_name
        self.tilt_value = tilt_value
        self.agg_pgd = agg_pgd
        self.raw_pgd_list = agg_pgd.raw_pgd_list

    def __str__(self):
        return str(self.summoner_name) + " " + str(self.tilt_value or -1) + " " + str(len(self.raw_pgd_list or []))
