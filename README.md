#School Selfie Station Prototype

The Selfie Station is meant to be an alternative to the headhunters you find on the top of ski resorts taking your picture. Instead of dealing with a person people could go up to a machine, swipe their phone or ski pass, get their picture taken and have it emailed and tweeted right to them.

![Selfie Selfie](/images/selfieSelfie.png)
##Parts Used

* [Raspberry Pi Model B+](https://www.sparkfun.com/products/12994)
* [Raspberry Pi Camera Module](https://www.sparkfun.com/products/11868)
* [Innovations ID-20LA RFID Reader](https://www.sparkfun.com/products/11828) (and [Jumper Wires](https://www.sparkfun.com/products/11710))

##Codebase

There's four core components of the Selfie Staiton: 

* The Camera
* The RFID Reader
* Emailing 
* Watermarking

Aside from those core parts, we used the standard Raspbian Debian Wheezy distrobution on the Raspberry Pi. The script is being ran on startup by running it on startup by adding 'python /home/pi/src/allPython.py' to the '/etc/rc.local' file.

###The Camera

Using the Raspberry Pi's camera module it was very simple to take a picture, adjust resolution, and other simple editting like horizontal and vertical flips. All of this is done via a Python interface written by [Dave Jones](https://twitter.com/waveform80). 

A more detailed explaination of the interface including some example code is available [here](http://www.raspberrypi.org/picamera-pure-python-interface-for-camera-module/) on the Raspberry Pi's official website.

###RFID Reader

We initially tried to use [Sparkfun's RFID USB Reader](https://www.sparkfun.com/products/9963) to connect the ID-20LA to the Raspberry Pi, however could not manage to get the D2XX drivers working for the board. So we opted to connect the reader directly to the GPIO pins on the Raspberry Pi.

In order to use the Reader in Python, we're using [µCasts' Raspberri Pi Library](https://github.com/sidwarkd/ucasts_pi) which was very easy to use. The `wait_for_scan()` function worked perfectly for what we needed. An extra thanks here to [Kevin "sidwarkd" Sidwar](https://github.com/sidwarkd) for not just writing the library, but also pointing out that the format pin needed to be connected.

####GPIO Connections

[ID12-LA Datasheet](http://dlnmh9ip6v2uc.cloudfront.net/datasheets/Sensors/ID/ID-2LA,%20ID-12LA,%20ID-20LA2013-4-10.pdf)

[Raspberry Pi GPIO Details](http://www.raspberrypi-spy.co.uk/2014/07/raspberry-pi-b-gpio-header-details-and-pinout/)

The only connections needed were Power, Ground, Data Transfer, and Format Selector. 

![RFID Pins](/images/RFIDPins.jpg)
![RFID Pins](/images/RPiPins.jpg)

Since these photos aren't the best here are the connections with the labels from the provided links.

| **Raspberry Pi Pins**    | **RFID Pins**         |
|-------------------------:|:----------------------|
| (3V3 Power) 1            | 11 (+2.8V thru +5.0V) |
| (Ground) 9               | 1 (GND)               |
| (Ground) 6               | 7 (Format Selector)   |
| (GPIO 15,  UART0_RXD) 10 | 9 (D0 Data Pin 0)     |


###Emailing

For emailing on the Raspberry Pi we went with a fairly basic SMTP method. In order to do multiple attachments and recepients we had to use some of the the built in `email.mime` functions in Python's standard library, specifically the Image, Text, and Multipart libraries.

###Tweeting

To send out our tweets we used this [guide](http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/) that uses the [Twython](https://github.com/ryanmcgrath/twython) API.

###Watermarking

We went with [ImageMagick](http://www.imagemagick.org/) to add a watermark to our photo. It's being done through a simple bash script using Imagemagick's CLI.














