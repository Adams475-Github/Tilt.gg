from riotwatcher import LolWatcher, ApiError
from bin import config


def setup(name, amount_of_games):
    api_key = config.api_key
    watcher = LolWatcher(api_key)
    my_region = 'na1'
    me = watcher.summoner.by_name(my_region, name)
    my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
    
    my_matches = watcher.match.matchlist_by_puuid(region='AMERICAS', puuid=me['puuid'])

    team = teammates(my_matches, watcher)
    for i in team:
            Lastmatches(amount_of_games, watcher, my_matches, i)



def teammates(my_matches, watcher):
    """Find Summoners and Kills in N past games"""
    j = 1
    thing = []
    thing = []
    Games = {}
    summoners = []
    stats = {}
    puuids = []
    thing = []
    #print("Game " + str(j) + "\n")
    test = watcher.match.by_id(region='AMERICAS', match_id=my_matches[j])
    i = 0
    while i <= 9:
        puuids.append(test['info']['participants'][i]['puuid'])

        i += 1
    k = -1
    stats.clear()
    for i in puuids:
        k += 1
        stats = {}
        stats["summ_name"] = watcher.summoner.by_puuid('na1', i)['name']
        thing.append(stats)
    Games["Game_" + str(j)] = thing
    #print(str(Games["Game_" + str(j)]) + "\n")
    for k in Games["Game_1"]:
        summoners.append(k['summ_name'])
    return summoners

















def Lastmatches(amount_of_games: int, watcher, my_matches, name):
    """Find Summoners and Kills in N past games"""
    j = 1
    thing = []
    summoners = []
    thing = []
    Games = {}
    while j <= amount_of_games:
        stats = {}
        puuids = []
        kills = []
        win = []
        deaths = []

        thing = []
        #print("Game " + str(j) + "\n")
        test = watcher.match.by_id(region='AMERICAS', match_id=my_matches[j])
        i = 0
        while i <= 9:
            puuids.append(test['info']['participants'][i]['puuid'])
            kills.append(test['info']['participants'][i]['kills'])
            win.append(test['info']['participants'][i]['win'])
            deaths.append(test['info']['participants'][i]['deaths'])

            i += 1
        k = -1
        stats.clear()
        for i in puuids:
            k += 1
            stats = {}
            stats["summ_name"] = watcher.summoner.by_puuid('na1', i)['name']
            stats["Kills"] = str(kills[k])
            stats["Win"] = str(win[k])
            stats["Deaths"] = str(deaths[k])
            thing.append(stats)
        Games["Game_" + str(j)] = thing
        #print(str(Games["Game_" + str(j)]) + "\n")
        j += 1
    summoners.append(Games)

    tiltscore(Games, name)
            
 
def tiltscore(Games, name):
    list1 = {}
    
    tilt = 0
    for i in Games:
        #print(i)
        for j in Games[i]:
            if j['summ_name'] == name:
                if j['Win'] == "False":
                    tilt += (int(j['Kills']) / (int(j['Deaths']) + .1) / 10) + 1
                else:
                   tilt += int(j['Kills']) / (int(j['Deaths'])+ .1) / 10

                   
            
    print(name + " - TILTSCORE: " + str(tilt))
    

    return


setup('JbeastJ', 3)




