import SummonerQueryUtils, PlayerGameData
#test
q = SummonerQueryUtils.SummonerQueryUtils("NA1", "hulksmash1337")
summoners_in_game = q.summoners_in_curr_game()
summoner_data = {}

for i in range(len(summoners_in_game)):
    summoner_data[summoners_in_game[i]] = None

for i in range(len(summoners_in_game)):
    squ = SummonerQueryUtils.SummonerQueryUtils("NA1", summoners_in_game[i])
    summoner_matches = squ.query_recent_games(3)
    playerDataList = []
    for j in range(len(summoner_matches)):
        playerData = PlayerGameData.PlayerGameData(summoner_matches[j], summoners_in_game[i])
        playerDataList.append(playerData)
    summoner_data[summoners_in_game[i]] = playerDataList

<<<<<<< Updated upstream
playerInstanceDataList = summoner_data[summoners_in_game[i]]
print(playerInstanceDataList)
#sumdeaths = None
#for i in range(len(playerInstanceDataList)):
    #sumdeaths += playerInstanceDataList[i].deaths
#sumdeaths /= len(playerInstanceDataList)
=======

playerInstanceDataList = summoner_data["Dizzydish"]
print(playerInstanceDataList[0].game_time)
print(playerInstanceDataList[1].deaths)
sumdeaths = 0
for i in range(len(playerInstanceDataList)):
    sumdeaths += playerInstanceDataList[i].deaths
sumdeaths /= len(playerInstanceDataList)

print(sumdeaths)
>>>>>>> Stashed changes
