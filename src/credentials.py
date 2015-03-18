##########################################################
#Twitter Information
##########################################################
__CONSUMER_KEY = 'YOUR CONSUMER KEY'
__CONSUMER_SECRET = 'YOUR CONSUMER SECRET'
__ACCESS_KEY = 'YOUR ACCESS KEY'
__ACCESS_SECRET = 'YOUR ACCESS SECRET'

def getConsumerKey():
	return __CONSUMER_KEY

def getConsumerSecret():
	return __CONSUMER_SECRET

def getAccessKey():
	return __ACCESS_KEY

def getAccessSecret():
	return __ACCESS_SECRET

##########################################################
#Gmail and SMTP Information
##########################################################
__EMAIL = "YOUR EMAIL"
__EMAILPASS = "YOUR EMAIL PASS"
__SMTP_HOST = "YOUR SMTP HOST" #gmail = "smtp.gmail.com"
__SMTP_PORT = "YOUR SMTP PORT" #gmail = 587

def getEmail():
	return __EMAIL

def getEmailPass():
	return __EMAILPASS

def getSMTPHost():
	return __SMTP_HOST

def getSMTPPort():
	return __SMTP_PORT
