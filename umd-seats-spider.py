Skip to content
This repository
Search
Pull requests
Issues
Gist
 @alexg636
 Unwatch 1
  Star 0
  Fork 0 alexg636/umd-seats-spider
 Code  Issues 0  Pull requests 0  Wiki  Pulse  Graphs  Settings
Branch: master Find file Copy pathumd-seats-spider/umd_seats_spider.py
e60839f  on May 17, 2015
@alexg636 alexg636 Third Commit
1 contributor
RawBlameHistory     99 lines (81 sloc)  3.68 KB

# University of Maryland waitlist spider - Fall 2015

# Meant for student use only

import requests
import time
from bs4 import BeautifulSoup
import smtplib
import getpass
import os

number_seats = 0
i = 1
course = raw_input('Which class would you like to crawl?\n')
seat_list = []

mail_decision = raw_input('\nWould you like: \n(1) gmail notification \n(2) text message notification (only Verizon or AT&T capability) \n(1 or 2): ')

if mail_decision == '1':
	username = 'openseats.spider@gmail.com'
	password = getpass.getpass()
	receiver = raw_input('Please enter your gmail address: ')
	
	mail = smtplib.SMTP('smtp.gmail.com',587)
	os.system('cls')	
		
	while number_seats == 0:
		print("\n**Start**")
		url = "https://ntst.umd.edu/soc/search?courseId=" + course + "&sectionId=&termId=201508&_openSectionsOnly=on&courseLevelFilter=ALL&instructor=&teachingCenter=ALL&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&creditCompare=&credits=&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"
		element = requests.get(url)
		plain = element.text
		soupObject = BeautifulSoup(plain)

		for seat in soupObject.findAll('span', {'class':'open-seats-count'}):
			number_seats = seat.string
			timer = str(time.strftime("%I:%M:%S"))	
			print('\n' + timer + '   ' + course.upper() + '  Number Open Seats: ' + number_seats)	
			number_seats = int(number_seats)
			seat_list.insert(i,number_seats)
			i += 1
		print("\n**Finish**")

		if number_seats > 0:
				new_seat_list = str(seat_list).strip('[]')
				new_seat_list = new_seat_list.replace(',', ' and')
				content = (('Hello there, ' + course.upper() + ' currently has ' + new_seat_list + ' open seat(s) to pick up!'))
				mail.starttls()
				mail.ehlo()
				mail.login(username,password)
				mail.sendmail(username,receiver,content)
				mail.close()
		elif number_seats == 0:
			time.sleep(900)
			
			
elif mail_decision == '2':
	username = 'openseats.spider@gmail.com'
	password = getpass.getpass()
	phone = raw_input('Choose your cellular provider (Verizon or AT&T): ')
	
	if phone.lower() == 'verizon':
		phone = '@vtext.com'
	elif phone.lower() == 'at&t':
		phone = '@txt.att.com'
	num = raw_input('Enter your phone number (no dashes): ')
	mail = smtplib.SMTP('smtp.gmail.com',587)
	os.system('cls')	
		
	while number_seats == 0:
		print("\n**Start**")
		url = "https://ntst.umd.edu/soc/search?courseId=" + course + "&sectionId=&termId=201501&_openSectionsOnly=on&courseLevelFilter=ALL&instructor=&teachingCenter=ALL&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&creditCompare=&credits=&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"
		element = requests.get(url)
		element = requests.get(url)
		plain = element.text
		soupObject = BeautifulSoup(plain)

		for seat in soupObject.findAll('span', {'class':'open-seats-count'}):
			number_seats = seat.string
			timer = str(time.strftime("%I:%M:%S"))	
			print('\n' + timer + '   ' + course.upper() + '  Number Open Seats: ' + number_seats)	
			number_seats = int(number_seats)
			seat_list.insert(i,number_seats)
			i += 1
		print("\n**Finish**")
		
		if number_seats > 0:
				new_seat_list = str(seat_list).strip('[]')
				new_seat_list = new_seat_list.replace(',', ' and')
				content = (('Hello there, ' + course.upper() + ' currently has ' + new_seat_list + ' open seat(s) to pick up!'))
				mail.ehlo()
				mail.starttls()
				mail.login(username,password)
				mail.sendmail(username,num+phone,content)
				mail.close()
		elif number_seats == 0:
			time.sleep(900) #sleeps for 15 minutes

Status API Training Shop Blog About
© 2016 GitHub, Inc. Terms Privacy Security Contact Help
