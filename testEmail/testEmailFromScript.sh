#!/bin/bash
SUBJECT="Webcam Watermark Test"
EMAIL="scheinmax@gmail.com"
#EMAIL="Joe.Corr@schoolhelps.com"
WATERMARK="School_Mark_2014_Color.png"
PHOTO="earth.jpg"
ATTACHMENT="earth-watermarked.jpg"
SNAPPHOTO="snapped.jpg"

imagesnap snapped.jpg
composite -compose atop -geometry +40 ./$WATERMARK ./$SNAPPHOTO ./$ATTACHMENT
mpack -s "$SUBJECT" $ATTACHMENT $EMAIL