import BackendIntellegence

live_game_player_tilt_profile_list = BackendIntellegence.get_live_game_tilt_metrics("NA1", "dd23438274")
for i in live_game_player_tilt_profile_list:
    print(i)
