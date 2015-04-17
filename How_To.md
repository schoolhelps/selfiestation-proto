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

####Rebooting the Raspberry Pi
In the command line:
```
sudo reboot
```
