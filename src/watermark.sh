#!/bin/bash
# $1 is watermark

composite -compose atop $1 $2 $3

#convert $PHOTO -resize 900 $RESIZE
#convert $RESIZE -crop 640x640+130+20 $CROPPED
