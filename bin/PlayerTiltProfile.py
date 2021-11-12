class PlayerTiltProfile:
    tilt_value = None
    summoner_name = None
    puuid = None
    agg_pgd = None
    raw_pgd_list = None
    lrgst_lss_stk = None
    curr_lss_stk = None

    def __init__(self, summoner_name, tilt_value, agg_pgd):
        self.summoner_name = summoner_name
        self.tilt_value = tilt_value
        self.agg_pgd = agg_pgd
        self.raw_pgd_list = agg_pgd.raw_pgd_list
        self.lrgst_lss_stk = agg_pgd.lrgst_lss_stk
        self.curr_lss_stk = agg_pgd.curr_lss_stk

    def __str__(self):
        return str(self.summoner_name) + " " + str(self.tilt_value or -1) + " " + str(len(self.raw_pgd_list or [])) + \
               " " + str(self.lrgst_lss_stk) + " " + str(self.curr_lss_stk)
