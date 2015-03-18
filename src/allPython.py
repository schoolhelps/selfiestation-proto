import smtplib
import picamera
import subprocess
import datetime
import os
import logging
import credentials
from ucasts import ID12LA
from time import sleep
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email import Encoders
from twython import Twython

path = os.getcwd() 
fun = False
if(len(sys.argv) > 1) and (sys.argv[1] == "fun"):
	fun = True

##########################################################
#The card controls how many pictures and videos are taken, as well as the picture and video properties
##########################################################
class Card:
	def __init__(self,cardIDinput):
		self.cardID = cardIDinput
		self.picHeight = 1000
		self.picWidth = 1000
		self.vidHeight = 480
		self.vidWidth = 640
		self.vidLength = 5
		self.picNum = 1
		self.vidNum = 0
		self.files = []
		self.email = 'selfie.station.pi@gmail.com'
		self.cardLookup()
	
	def setPicHW(self, h, w):
		self.picHeight = h
		self.picWidth = w

	def setVidHWL(self, h, w, l):
		self.vidHeight = h
		self.vidWidth = w
		self.vidLength = l

	def setPicNum(self, n):
		self.picNum = n

	def setVidNum(self, n):
		self.vidNum = n

	def getEmail(self):
		return self.email

	def getFiles(self):
		return self.files

	def getID(self):
		return self.cardID

	def cardInstructions(self):
		self.files.extend(take_multiple_pictures(self.picNum, self.picHeight, self.picWidth))
		for x in range(0, self.vidNum):
			self.files.extend(take_video(self.vidHeight, self.vidWidth, self.vidLength))

	def cardLookup(self):
		if(self.getID()[-1:] == '3'):
			self.setVidNum(1)
			self.setPicNum(0)

##########################################################
#Email and Twitter Section
##########################################################
def send_mail(send_from, send_pass, send_to, subject, files, bodyText):

	to = send_to

	gmailUser = send_from
	gmailPass = send_pass

	s = smtplib.SMTP(credentials.getSMTPHost(),credentials.getSMTPPort())
	s.ehlo()
	s.starttls()
	s.ehlo
	s.login(gmailUser, gmailPass)
	
	logging.info(get_timestamp() + "Successfully logged into Gmail.")

	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = gmailUser
	msg['To'] = ", ".join(to)

	msg.attach(MIMEText(bodyText))
	i = 1
	for f in files:
		part = MIMEBase('application',"octet-stream")    
                fo = open(f,"rb")
                part.set_payload(fo.read())
                fo.close()
		Encoders.encode_base64(part)
		if(f[-1:] == '4'):
			ext = f[-5:]
		else:
			ext = f[-4:]
		namedFile = "Selfie_"+str(i)+ext
                part.add_header('Content-Disposition', 'attachment;', filename=namedFile)
                msg.attach(part)
		i += 1

	logging.info(get_timestamp() + "Email sending.")
	s.sendmail(gmailUser, to, msg.as_string())
	logging.info(get_timestamp() + "Email sent.")
	s.close()

def tweet_photo(filePhoto, text):
	logging.info(get_timestamp() + "Tweeting: " + filePhoto)
	CONSUMER_KEY = credentials.getConsumerKey()
	CONSUMER_SECRET = credentials.getConsumerSecret()
	ACCESS_KEY = credentials.getAccessKey()
	ACCESS_SECRET = credentials.getAccessSecret() 

	api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 
	photo = open(filePhoto,'rb')

	tweet_txt = text
	media_status = api.upload_media(media=photo)
	api.update_status(media_ids=[media_status['media_id']], status=tweet_txt)

def multiple_tweets(files,text):
	logging.info(get_timestamp() + "Tweeting Multiple Photos.")
	for i in files:
		if(check_file_for_tweet()):
			tweet_photo(i,text)

def check_file_for_tweet(file):
	if(file[-1:] == '4'):
		return False
	else:
		return True

##########################################################
#Camera and Watermarking Section
##########################################################
def take_picture(width, height):
	camera = picamera.PiCamera()
	camera.resolution = (width, height)
	pictureName = path+'/picameraPic'+get_file_timestamp()+'.jpg'
	
	camera.start_preview()
	blink(camera,4,.15)
	camera.capture(pictureName)
	camera.stop_preview()
	camera.close()
	logging.info(get_timestamp() + "Picture captured: "+pictureName)

	return pictureName

def watermark_picture(picameraPic):
	watermarkPhoto = path+ '/School_Watermark.png'
	photo = picameraPic
	result = path+'/watermark'+get_file_timestamp()+'.jpg'
	watermarkCall = path+"/addWatermark.sh " + watermarkPhoto + " " + photo + " " + result

	subprocess.call(watermarkCall, shell=True)
	logging.info(get_timestamp() + "Watermark on "+ photo + " successful, created: "+ result)

	return result

def take_video(h,w,l):
	videoFile = path+'/piVideo'+get_file_timestamp()+'.h264'
	logging.info(get_timestamp() + "Recording video: "+videoFile)
	with picamera.PiCamera() as camera:
		blink(camera, 10, .05)
		camera.resolution = (h,w)
		camera.start_recording(videoFile)
		camera.wait_recording(l)
		camera.stop_recording()
	logging.info(get_timestamp() + "Finished recording video.")
	return [videoFile]

def blink(camera, count, interval): #Blinks the camera's LED
	for i in range(0, count):
                camera.led = False
                sleep(interval)
                camera.led = True
		sleep(interval)

def take_single_picture(h,w):
	return [watermark_picture(take_picture(h,w))]

def take_multiple_pictures(count,h,w):
	files = []
	for x in range(0, count):
		files.extend(take_single_picture(h,w))
	return files

##########################################################
#Misc. Section
##########################################################
def get_timestamp():
	return datetime.datetime.now().strftime("%H:%M %b %d, %Y")

def get_file_timestamp():
	return datetime.datetime.now().strftime("%H%M%b%d%Y%f")

def remove_local_files():
	subprocess.call("rm -f picameraPic*",shell=True)
	subprocess.call("rm -f watermark*",shell=True)
	subprocess.call("rm -f piVideo*",shell=True)

##########################################################
#Most important section
##########################################################
def funky_dance_party():
	camera = picamera.PiCamera()
	camera.led = False
	funky_dance_party_lights(camera)
	camera.close()

def funky_dance_party_lights(camera):	
	blink(camera,3,.3)	
	for i in range(1,4):	
		blink(camera,7,.025*i)
	for i in range(1,4):	
		blink(camera,8,.025*i)
	for i in range(1,4):	
		blink(camera,9,.025*i)
	blink(camera,1,.8)	
	for i in range(1,4):	
		blink(camera,11,.025*i)
	blink(camera,3,.3)
	for i in range(1,4):	
		blink(camera,11,.025*i)
	blink(camera,1,.8)	

##########################################################
#Driver Section
##########################################################
logging.basicConfig(filename=path+'/errorLog.log',level=logging.DEBUG)
logging.info("Process starting at " + get_timestamp() )

reader = ID12LA() #RFID Reader

selfieStationEmail = credentials.getEmail()
selfieStationPass = credentials.getEmailPass()
send_to = ["selfie.station.pi@gmail.com"]
files = []

while(not fun):
	logging.info(get_timestamp() + "Ready for new scan.")
	print "Awaiting scan"
	tag = reader.wait_for_scan()
	if tag != None:
		logging.info(get_timestamp() + "Tag found: "+tag)
		print "Card", tag, "found, initializing selfie protocol."
	
		currentCard = Card(tag)
		currentCard.cardInstructions()
		files = currentCard.getFiles()
		
		multiple_tweets(files, "Selfie(s) from " + get_timestamp())

		subject = "Selfie(s) from " + get_timestamp()
		text = "Here's your selfie(s), " + tag
		send_to.append(currentCard.email)
		print "Emailing ", send_to, " selfie."
		logging.info(get_timestamp() + "Emailing selfie to: " + send_to)
		send_mail(selfieStationEmail, selfieStationPass, send_to, subject, files,text)

		send_to = ['selfie.station.pi@gmail.com']	
		tag = None
		remove_local_files()
		files = []

while(fun):
	print 'Commencing light show'
	funky_dance_party()
