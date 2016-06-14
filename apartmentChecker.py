from bs4 import BeautifulSoup
import requests
import re

def aptSpider():
	URL = 'http://www.avaloncommunities.com/virginia/reston-herndon-apartments/avalon-reston-landing/apartment/VA565-VA565-010-0105'
	element = requests.get(URL)
	plainText = element.text
	soupObject = BeautifulSoup(plainText, "lxml")
	for target in soupObject.find_all('div', {'class':'description'}):
		targetTXT = str(target)
	result = re.search('Available (.*)', targetTXT)
	dateHTML = result.group(1)

	dateTarget = '5/11/2016' # Put whatever date here

	if dateTarget in dateHTML:
		print "DATE AVAILABLE!!!"
	else:
		print "Date not available"

aptSpider()
