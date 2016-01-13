
from bs4 import BeautifulSoup
import requests as rq
import urllib2
import sys

base_url = "http://www.genius.com"
artist = "/albums/Kanye-west"
album = "/Yeezus"

YEEZUS = []
COLLEGE_DROPOUT = []

try:
	req = urllib2.Request(base_url + "d" + album, headers={ 'User-Agent': 'Mozilla/5.0' })
	html = urllib2.urlopen(req).read()
	soup = BeautifulSoup(html, "lxml")
except urllib2.URLError:
	print("Invalid artist or album")
	sys.exit(0)

print(stopped)
songs = [link['href'] for link in soup.findAll("a", {"class": "song_name published   song_link"})]

for song in songs:
	print song
