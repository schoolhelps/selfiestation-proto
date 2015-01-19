#!/bin/bash
BASE="base.jpg"
IMAGE="right.jpg"
MASK="mask.png"
FUZZ="1%"
RESULT="result1.png"

compare -metric AE -fuzz $FUZZ $BASE $IMAGE -compose Src -highlight-color White -lowlight-color Black $MASK

convert $BASE $IMAGE $MASK -compose multiply -composite $RESULT