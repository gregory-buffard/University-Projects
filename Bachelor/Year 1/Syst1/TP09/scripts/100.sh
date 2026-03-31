#!/bin/zsh

vared -p "Enter a number: " -c input

if [ $input -lt 100 ]; then
	echo "Less than 100."
elif [ $input -gt 100 ]; then
	echo "Greater than 100."
elif [ $input -eq 100 ]; then
	echo "Equal to 100."
else
	echo "Not a number dumbass."
fi
