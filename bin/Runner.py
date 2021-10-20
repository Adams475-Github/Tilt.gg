from bin import QueryUtils

q = QueryUtils.QueryUtils("na1")
# matches = q.query_recent_games(summoner_name="hulksmash1337", amount=20)
print(q.summoners_in_curr_game("hulksmash1337"))

