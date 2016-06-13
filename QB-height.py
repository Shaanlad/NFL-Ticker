#!python
#find the name, height of all QB
import xml.etree.ElementTree as ET
tree = ET.parse('Fantasy-NFL-QB-Players.xml')
root = tree.getroot();

for player in root.findall('Player'):
	fname = player.get('fname')
	lname = player.get('lname')
	team = player.get('team')
	height = player.get('height')	
	print fname, lname, team, height