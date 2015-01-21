##Raspi Setup

1. [Install OS](http://www.raspberrypi.org/help/noobs-setup/)
2. [Setup Camera](http://www.raspberrypi.org/documentation/usage/camera/README.md)
3. Watermarks
4. Emailing
5. [Setup RFID Reader](https://www.sparkfun.com/tutorials/243) ([Drivers](http://www.ftdichip.com/FTDrivers.htm))
6. Script it all together

[Parts](https://docs.google.com/document/d/1Aqv9FwogubRNbwb0DYq8632tRPEbR4dWg0ym3a4JpQk/edit?usp=sharing)

[MySQL Hosting](http://www.freemysqlhosting.net/)

##Software

1. Python script checking for RFID read
2. (Event) RFID Scanned
3. Python saves RFID number, does a look up for the user
4. Bash Script takes photo(s) and watermarks.
5. Python Emails photo(s).
6. Python returns to waiting for RFID read.

##Camera

[Raspistill bash](http://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md)

[Timelapse](http://www.raspberrypi.org/documentation/usage/camera/raspicam/timelapse.md) if we want to do one.

For prototyping on the Mac [Imagesnap](http://osxdaily.com/2007/01/24/capture-isight-images-using-the-command-line/) 
```
brew install imagesnap
```

##Emailing

####Method #1
[mpack & SSMTP](http://ozzmaker.com/2012/12/03/send-email-from-the-raspberry-pi-or-linux-command-line-with-attachments/)

####Method #2 (Allows for multiple attachments)
[mailx](http://www.fclose.com/5167/sending-email-using-mailx-in-linux-through-internal-smtp/)

```
(uuencode $FILE1 $FILE1; uuencode $FILE2 $FILE2; uuencode $FILE3 $FILE3)|mailx -s"Sending Three Attachments" $EMAIL
```

####Method #3
[Mutt](http://www.maclife.com/article/columns/terminal_101_using_mutt_email_client) (OS X) 
```
sudo apt-get update
sudo apt-get install mutt
```

####Method #4
[Twitterbot](http://www.instructables.com/id/Raspberry-Pi-Twitterbot/?ALLSTEPS)

##Watermark, Resize, and Crop

####Imagemagick
---
(Linux) Install:
```
sudo apt-get update
sudo apt-get install imagemagick --fix-missing
```
---
Resize
```
convert original.jpg -resize 900 resized.jpg
```
---

Crop
```
convert original.jg -crop 640x640+130+20 cropped.jpg
                                  ^X, Y offset
```

---

Watermark
```	
composite -compose atop -geometry +75 -gravity southeast ./watermark.png ./photo.jpg ./photo-watermarked.jpg
```

```
-geometry +123	# moves the image being overlayed
atop			# makes image ‘over’ and keeps original size
-gravity <direction>	# where to overlay, default is northwest
```

(From [here](http://www.xoogu.com/2013/how-to-automatically-watermark-or-batch-watermark-photos-using-imagemagick/). Includes a bash script to do something similar.)
