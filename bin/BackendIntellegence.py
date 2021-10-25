import Utils
import PlayerTiltProfile


def get_live_game_tilt_metrics(region, summoner_name):
    agg_pgd_list = Utils.get_live_game_agg_pgd_list(region, summoner_name)
    live_game_summoner_tilt_profile_list = []
    for agg_pgd in agg_pgd_list:  # TODO
        tilt_value = 0
        tilt_value += agg_pgd.losses
        tilt_value += agg_pgd.avg_int * 4
        tilt_value += agg_pgd.avg_deaths
        live_game_summoner_tilt_profile_list.append(PlayerTiltProfile.PlayerTiltProfile(agg_pgd.summoner_name,
                                                                                        tilt_value, agg_pgd))
    return live_game_summoner_tilt_profile_list
