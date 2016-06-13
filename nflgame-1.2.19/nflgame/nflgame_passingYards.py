#!python
import nflgame

games = nflgame.games(2013, week=1)
plays = nflgame.combine_plays(games)

#value = getattr(nflgame, "first_name")
# Pull data from nflgame where name is T.Brady - use a query where clause (use of conditions)
# Retrieve architecture - JSON, XML


for p in plays.sort('passing_yds').limit(5):
    print p