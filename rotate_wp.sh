#! /bin/bash
export DISPLAY=:0.0
WALLPAPERS="/usr/share/backgrounds"
ALIST=( `ls -w1 $WALLPAPERS | grep jpg` )
RANGE=${#ALIST[@]}
echo $ALIST
echo $RANGE
let "number = $RANDOM"
let LASTNUM="`cat $WALLPAPERS/.last` + $number"
let "number = $LASTNUM % $RANGE"
echo $number > $WALLPAPERS/.last
nitrogen --set-scaled --save $WALLPAPERS/${ALIST[$number]}
