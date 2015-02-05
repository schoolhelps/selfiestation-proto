import smtplib
import picamera
import subprocess
from ucasts import ID12LA
from time import sleep
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_mail(send_from, send_pass, send_to, subject, files):

	to = send_to

	gmailUser = send_from
	gmailPass = send_pass

	s = smtplib.SMTP("smtp.gmail.com",587)
	s.ehlo()
	s.starttls()
	s.ehlo
	s.login(gmailUser, gmailPass)
	
	print "Logged into Gmail."

	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = gmailUser
	msg['To'] = ", ".join(to)

	for f in files:
		fp = open(f, 'rb')
		img = MIMEImage(fp.read())
		fp.close()
		msg.attach(img)

	print "Email sending."
	s.sendmail(gmailUser, to, msg.as_string())
	print "Email sent."
	s.close()

def take_picture(width, height):
	camera = picamera.PiCamera()
	camera.resolution = (width, height)
	camera.start_preview()
	sleep(3)
	camera.capture('/home/pi/src/picameraPic.jpg')
	print "Selfie captured."
	camera.stop_preview()
	camera.close()
	return '/home/pi/src/picameraPic.jpg'

def watermark_picture(picameraPic):
	watermarkPhoto = '/home/pi/src/School_Watermark.png'
	photo = picameraPic
	result = '/home/pi/src/watermarked.jpg'
	watermarkCall = "/home/pi/src/watermark.sh " + watermarkPhoto + " " + photo + " " + result
	subprocess.call(watermarkCall, shell=True)
	print "Watermark Successful."
	return result

sleep(10)

reader = ID12LA()

selfieStationEmail = "selfie.station.pi@gmail.com"
selfieStationPass = "spring2015"
send_to = ["selfie.station.pi@gmail.com"]
subject = "Testing params & Files"
files = []

while(True):
	print "Awaiting scan"
	tag = reader.wait_for_scan()
	if tag != None:
		print "Card", tag, "found, initializing selfie protocol."
		files.append(watermark_picture(take_picture(1000,1000)))
		print "Emailing ", send_to, " selfie."
		send_mail(selfieStationEmail, selfieStationPass, send_to, subject, files)
		tag = None
		files = []

