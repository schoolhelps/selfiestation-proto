
##Raspi Setup

[SSH, telnet, HTTP](http://dcoj.wmh3.com/geekstuff/pisu/1.html)

##Camera

[Setup](http://www.raspberrypi.org/documentation/usage/camera/README.md)

[Raspistill bash](http://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md)

[Timelapse](http://www.raspberrypi.org/documentation/usage/camera/raspicam/timelapse.md) if we want to do one.


##Emailing

####Method #1
[mpack & SSMTP](http://ozzmaker.com/2012/12/03/send-email-from-the-raspberry-pi-or-linux-command-line-with-attachments/)

####Method #2
[Mutt](http://www.maclife.com/article/columns/terminal_101_using_mutt_email_client) (OS X) 
```
sudo apt-get update
sudo apt-get install mutt
```

####TwitterBot
[Instructable](http://www.instructables.com/id/Raspberry-Pi-Twitterbot/?ALLSTEPS)

##Watermarking

####Imagemagick

(Linux) Install:
```
sudo apt-get update
sudo apt-get install imagemagick --fix-missing
```

Watermark a small image
```	
composite -compose atop -geometry +75 -gravity southeast ./watermark.png ./photo.jpg ./photo-watermarked.jpg
```

```
-geometry +123	# moves the image being overlayed
atop			# makes image ‘over’ and keeps original size
-gravity <direction>	# where to overlay, default is northwest
```

(From [here](http://www.xoogu.com/2013/how-to-automatically-watermark-or-batch-watermark-photos-using-imagemagick/). Includes a bash script to do something similar.)


