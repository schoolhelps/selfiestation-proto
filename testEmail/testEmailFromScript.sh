#!/bin/bash
SUBJECT="Webcam Watermark Test"
EMAIL="larryrubin93@gmail.com"
#EMAIL="Joe.Corr@schoolhelps.com"

WATERMARK="School_Mark_2014_Color.png"
ATTACHMENT="photo.jpg"

FILEPHOTO="earth.jpg" #from file
SNAPPHOTO="snapped.jpg" #from webcam

RESIZE="resize.jpg"
CROPPED="cropped.jpg"
#WATERMARKED="watermarked.jpg"

imagesnap snapped.jpg
convert $SNAPPHOTO -resize 900 $RESIZE
convert $RESIZE -crop 640x640+130+20 $CROPPED
composite -compose atop -geometry +40 ./$WATERMARK ./$CROPPED ./$ATTACHMENT
mpack -s "$SUBJECT" $ATTACHMENT $EMAIL
