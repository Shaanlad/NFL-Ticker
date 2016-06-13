#!python
import nflgame

games = nflgame.games(2015, week=16)
players = nflgame.combine_game_stats(games)

# msg_2 = '%s %d carries for %d yards and %d TDs' where first_name = 'Tom Brady'
# print msg_2

for p in players.rushing().sort('rushing_yds').limit(5):
    msg = '%s %d carries for %d yards and %d TDs'    
    print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)

