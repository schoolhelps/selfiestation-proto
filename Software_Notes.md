


##Watermarking:

####Imagemagick:

Install:
```
sudo apt-get update
sudo apt-get install imagemagick --fix-missing
```

```	
composite -compose atop -geometry +75 -gravity southeast ./watermark.png ./photo.jpg ./photo-watermarked.jpg
```

```
-geometry +123	# moves the image being overlayed
atop			# makes image ‘over’ and keeps original size
-gravity <direction>	# where to overlay, default is northwest
```




