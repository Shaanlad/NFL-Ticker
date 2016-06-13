#!python
#find the NFL News - title, description, link, publishingDate
import urllib2
import xml.etree.ElementTree as ET
tree = ET.ElementTree(file=urllib2.urlopen('http://espn.go.com/espn/rss/nfl/news'))
root = tree.getroot();

for item in root.findall('Item'):
	title = item.get('title')
	description = item.get('description')
	link = item.get('link')
	publishingDate = item.get('pubDate')	
	print title, description, link, publishingDate
