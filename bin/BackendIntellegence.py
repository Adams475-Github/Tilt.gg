import Utils


def live_game_tilt_metrics(region, summoner_name):
    agg_pd = Utils.get_agg_pd(region, summoner_name)
    summoner_tilt_pairs = {}
    for i in agg_pd:
        tilt_value = 0
        tilt_value += agg_pd[i].losses
        summoner_tilt_pairs[i] = tilt_value

    return summoner_tilt_pairs
