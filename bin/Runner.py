import BackendIntellegence
import Utils
import PlayerGameData

# gameData = BackendIntellegence.live_game_tilt_metrics("NA1", "Kìmchì")

# gameData = BackendIntellegence.live_game_tilt_metrics("NA1", "mieuk")
# print(gameData)

squ = Utils.SummonerQueryUtils("NA1", "Peach ToadstooI")
recent_games = squ.recent_games(10)
l = []
for i in range(len(recent_games)):
    l.append(PlayerGameData.RawPGD(recent_games[i], "Peach ToadstooI"))
for i in range(len(l)):
    print(l[i])
