from bs4 import BeautifulSoup
import requests
import re
import os

os.system('cls')
choice = 'y'

while choice == 'y':
	print 'Music Map'
	print '~~~~~~~~~\n'
	band_original = raw_input('Name of the band: ')
	band_edit = band_original.replace(' ', '+')

	url = 'http://www.music-map.com/' + band_edit + '.html'	
	element = requests.get(url)
	plain_text = element.text
	soupObject = BeautifulSoup(plain_text)
	for band_name in soupObject.findAll('a'):
		band_name = (band_name.get_text())
		if band_name == 'Music-Map':
			continue
		elif band_name == '?':
			continue
		elif band_name == band_original.title():
			print ''
		else:
			print (band_name.encode("utf-8"))
			
	choice = raw_input('\nWould you like to make another search? \n(y/n): ')
	if choice == 'n':
		os.system('exit')
	elif choice == 'y':
		os.system('cls')

