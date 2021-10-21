from bin import SummonerQueryUtils

q = SummonerQueryUtils.SummonerQueryUtils("NA1", "hulksmash1337")
matches = q.query_recent_games(amount=20)
print(q.summoners_in_curr_game())

