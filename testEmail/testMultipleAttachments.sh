#!/bin/bash
FILE1="planets.jpg"
FILE2="earth.jpg"
FILE3="School_Mark_2014_Color.png"
EMAIL="larryrubin93@gmail.com"

(uuencode $FILE1 $FILE1; uuencode $FILE2 $FILE2; uuencode $FILE3 $FILE3)|mailx -s"Testing Attachments #2 with Mailx" larryrubin93@gmail.com