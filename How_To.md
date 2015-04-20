####Connecting to the Raspberry Pi from command line
In the command line:
```
ssh pi@
```
When it prompts it should ask for a password, it is `raspberry`

####Editing run time files from command line

Connect to the Pi with the above instructions then:
```
cd src
vim file.txt
```
Move the cursor with the arrow keys. Press `i` to toggle editing on. Press `esc` to toggle editing off. To save and quit press `:wq` followed by `enter`. To quit without saving press `:q!` followed by `enter`.

####Adding an email
Just add a new line to the 'emailList.txt' file with the email. Example:

```
existingemail@gmail.com
```
to
```
existingemail@gmail.com
newemail@gmail.com
```

####Changing the watermark file
Move the desired png file to your desktop. Open a new terminal window and do the following command with \<Your Name> replaced with your computer's user name (use the `pwd` command to check what that is if you're unsure), and the first New_Watermark.png with the filname of the watermark photo:
```
scp /Users/<Your Name>/Desktop/New_Watermark.png pi@:/home/pi/src/New_Watermark.png
```
You should be prompted for a password, it's also `raspberry`.
Then connect to the Raspberry Pi, and edit the sourceWatermark.txt file to read (replace the current line):
```
New_Watermark.png
```
Note: This will default to a few pixels to the right of the the top left corner, it can be changed in the code or by using a transparent png the size of the photo (1000px by 1000px) with the watermark in it's proper spot.
####Rebooting the Raspberry Pi
In the command line:
```
sudo reboot
```
If it prompts for a password it's `raspberry`.
