Skip to content
This repository
Search
Pull requests
Issues
Gist
 @alexg636
 Unwatch 1
  Star 0
  Fork 0 alexg636/subreddit_notification
 Code  Issues 0  Pull requests 0  Wiki  Pulse  Graphs  Settings
Branch: master Find file Copy pathsubreddit_notification/subreddit_notification.py
fda81ca  on Oct 22, 2015
@alexg636 alexg636 local file
1 contributor
RawBlameHistory     85 lines (63 sloc)  1.78 KB
import praw
import time
import os
import smtplib
import getpass

# CHANGE AS NEEDED
TEXT_PATH = '/Users/alexgeorge/Dropbox/Python/test.txt'

def lines(file_name):
	with open(file_name) as g:
		return sum(1 for _ in g) 

# SMTP setup
username = 'alexjgeorge636@gmail.com'
password = getpass.getpass()
phone = raw_input('Choose your cellular provider (Verizon/AT&T/Tmobile): ')

if phone.lower() == 'verizon':
	phone = '@vtext.com'
elif phone.lower() == 'at&t':
	phone = '@txt.att.com'
elif phone.lower() == 'tmobile':
	phone = '@tmomail.net'
phone_num = raw_input('Enter your ten digit phone number (no dashes): ')
mail = smtplib.SMTP('smtp.gmail.com',587)
os.system('clear')

subred = raw_input('Which subreddit would you like to crawl?\n')
WORD = raw_input('What keyword would you like to scrape /r/' + subred + ': ')
os.system('clear')
print 'Searching /r/' + subred + ' for ' + WORD
print 'Alert set to ' + phone_num + '\n'



while True:

	titles = []
	keyword = []
	pos = []

	i = 0
	j = 0


	r = praw.Reddit(user_agent = 'keyword scraper by /u/xela636')
	posts = r.get_subreddit(subred).get_new(limit = 25)

	for item in posts:
		titles.append(str(item).lower())

	for item in titles:
		if WORD.lower() in item:
			pos.append(i)
		i += 1

	for nums in pos:
		keyword.append(titles[nums])

	initial_lines = lines(TEXT_PATH)

	for entry in keyword:
		if entry not in open(TEXT_PATH).read():
			f = open(TEXT_PATH, 'a')
			f.write(entry + '\n')
			f.close()
			print '\n' + entry

	final_lines = lines(TEXT_PATH)
	calc = final_lines - initial_lines
	if calc > 0:
			content = str(calc) + ' new deal(s) for ' + WORD
			mail.ehlo()
			mail.starttls()
			mail.login(username,password)
			mail.sendmail(username,phone_num+phone,content)
			mail.close()
	else:
		print 'Nothing new'

	print '********WAITING********\n'	

	time.sleep(300)

Status API Training Shop Blog About
© 2016 GitHub, Inc. Terms Privacy Security Contact Help
