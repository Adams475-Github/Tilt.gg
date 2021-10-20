from bin import QueryUtils

q = QueryUtils.QueryUtils("na1")
matches = q.query_recent_games(summoner_name="hulksmash1337", amount=20)

