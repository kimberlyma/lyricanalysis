import sys
from bs4 import BeautifulSoup
import requests as rq
import urllib2

class RapGeniusLyrics(object):
	"""Description here

	Attributes:
	artist: A string that represents the artist name
	albums: A list of albums
	"""
	BASE_URL = "http://www.genius.com/albums/"

	def __init__(self, *args):
		self.format_artist_name(args[0])
		self.albums = []
		for elem in args[1:]:
			self.format_album_name(elem)
		self.generate_soup()
		self.traverse_albums()

	def format_artist_name(self, name):
		self.artist = name.replace(" ", "-")

	def format_album_name(self, album):
		self.albums.append(album.replace(" ", "-"))


	def generate_soup(self):
		self.album_links = {}
		for album in self.albums:
			try:
				req = urllib2.Request(self.BASE_URL + self.artist + '/' + album, headers={ 'User-Agent': 'Mozilla/5.0' })
				html = urllib2.urlopen(req).read()
				soup = BeautifulSoup(html, "lxml")
			except urllib2.URLError:
				print("Invalid artist or album")
				sys.exit(0)
			self.album_links[album] = soup
			self.album_links[album] = [link['href'] for link in soup.findAll("a", {"class": "song_name published   song_link"})]
	
	def traverse_albums(self):
		for k, v in self.album_links.iteritems():
			print k
			print v

	def pull_lyrics(album_links):
		for song in album_links:
			current_episode = rq.get(base_url + episode)
			soup_new = BeautifulSoup(current_episode.text, "lxml")
			txt = soup_new.getText()
			return txt
