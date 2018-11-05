#!/usr/bin/env python36

####
#name: lior
#
#
####


import smtplib
import getpass

user_mail = input('please enter your gmail:')
user_pass = getpass.getpass('enter your password')

rec_mail = input('please enter to reciver mail') 
subject = input('please enter a subject')

#get a long string content
print('plese enter your content, to stop hit ctrl + d')
body = []

while True:
	try:
		line = input()
	except EOFError:
		break
	body.append(line)
body = '\n'.join(body)
		 
the_mail = 'Subject: {}\n\n {}'''.format(subject, body)

try:
	server_mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server_mail.ehlo()
	server_mail.login(user_mail, user_pass)
	server_mail.sendmail(user_mail, rec_mail, the_mail)
	server_mail.close()
	print('mail send')
except:
	print('something went worng')
