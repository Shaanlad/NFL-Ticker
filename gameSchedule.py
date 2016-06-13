#!python
#find the gameDate, homeTeam, awayTeam, gameTime in ET
import xml.etree.ElementTree as ET
tree = ET.parse('Fantasy-NFL-Game-Schedule.xml')
root = tree.getroot();

for game in root.findall('Game'):

	gameDate = game.get('gameDate');
	homeTeam = game.get('homeTeam');
	awayTeam = game.get('awayTeam');
	gameTimeinET = game.get('gameTimeET');

	print gameDate	

	# print gameDate
	# print homeTeam + "vs" + awayTeam
	# print gameTimeinET
	# print " --- "