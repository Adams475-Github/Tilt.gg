import Utils


def live_game_tilt_metrics(region, summoner_name):
    agg_pd = Utils.get_agg_pd(region, summoner_name)
    ptml = Utils.tilt_agg(agg_pd)  # Player Tilt Metrics List
    return ptml
