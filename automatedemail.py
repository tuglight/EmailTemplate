import csv
import getpass
import smtplib
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def GetUserInfo():
	fromAddress = input('Please enter your email address: ')
	password = getpass.getpass('Please enter your password: ')
	from_first_name = input('Please enter your first name: ')
	from_last_name = input('Please enter your last name: ')
	return fromAddress, password, from_first_name, from_last_name

def GetEmailDetails():
	recipientsFile = input('Please enter the recipient list CSV file: ')
	messageFile = input('Please enter the message file you wish to send: ')
	subject = input('Please enter the subject heading for the email: ')
	return recipientsFile, messageFile, subject

def ReplaceEmailBody(textBody, to_first_name, to_last_name, from_first_name, from_last_name):
	textBody = textBody.replace("to_first_name", to_first_name)
	textBody = textBody.replace("to_last_name", to_last_name)
	textBody = textBody.replace("from_first_name", from_first_name)
	textBody = textBody.replace("from_last_name", from_last_name)
	return textBody

def PrintConfirmation(first_name, last_name, recipientsFile, body):
	print(first_name, last_name, 'you are about send an email formatted below to the recipients in', recipientsFile, ':')
	print(body)
	confirm = input('Is this correct to send? (y/n): ')
	return confirm

def GetSMTPAndPort(fromAddress):
	if '@gmail.com' in fromAddress:
		smtpServer = 'smtp.gmail.com'
		port = 587
	# elif '@yahoo.com' in fromAddress:
	# 	smtpServer = 'smtp.mail.yahoo.com'
	# 	port = 587
	# elif '@live.com' in fromAddress:
	# 	smtpServer = 'smtp.live.com'
	# 	port = 587
	# elif '@hotmail.com' in fromAddress:
	# 	smtpServer = 'smtp.live.com'
	# 	port = 587
	else:
		smtpServer = input('Please enter your SMTP server: ')
		port = input('Please enter your port number: ')
	return smtpServer, port

recipientsList = []
fromAddress, password, from_first_name, from_last_name = GetUserInfo()
recipientsFile, messageFile, subject = GetEmailDetails()



with open(recipientsFile, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        recipientsList.append(row)

messageFile = open(messageFile,"r")
body = messageFile.read()

confirm = PrintConfirmation(from_first_name, from_last_name, recipientsFile, body)

if confirm == 'y' or confirm == 'Y':
	smtpServer, port = GetSMTPAndPort(fromAddress)
	server = smtplib.SMTP(smtpServer, port)
	server.starttls()
	try:
		server.login(fromAddress, password)
	except smtplib.SMTPAuthenticationError:
		print('Your username/password combination probably was not accepted!')
		print('Now exiting...')
		sys.exit()

	msg = MIMEMultipart()

	for recipients in recipientsList:
		msg = MIMEMultipart()
		msg['From'] = fromAddress
		msg['To'] = recipients['email_address']
		msg['Subject'] = subject
		modifiedBody = body
		modifiedBody = ReplaceEmailBody(modifiedBody, recipients['first_name'], recipients['last_name'], from_first_name, from_last_name)
		msg.attach(MIMEText(modifiedBody, 'plain'))
		text = msg.as_string()
		toAddress = recipients['email_address']
		server.sendmail(fromAddress, toAddress, text)
		msg = ""
	server.quit()
	print('Messages sent.  Now exiting...')
else:
	print('Message not sent.  Now exiting...')
