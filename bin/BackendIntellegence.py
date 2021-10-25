import Utils
import PlayerTiltProfile


def get_live_game_tilt_metrics(region, summoner_name):
    agg_pd = Utils.get_live_game_agg_pgd_list(region, summoner_name)
    live_game_summoner_tilt_profile_list = []
    for i in agg_pd:
        tilt_value = 0
        tilt_value += agg_pd[i].losses
        tilt_value += agg_pd[i].avg_int * 4
        tilt_value += agg_pd[i].avg_deaths
        live_game_summoner_tilt_profile_list.append(PlayerTiltProfile.PlayerTiltProfile(i, tilt_value, agg_pd[i]))

    return live_game_summoner_tilt_profile_list
