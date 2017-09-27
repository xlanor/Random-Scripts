#! /usr/bin/env python3
#-*- coding: utf-8 -*-
##
# exam score text
# Written by xlanor
# to help someone with homework.
##

class examscore():
	def calcgrade(self,score):
		score = float(score)
		if score >= 85:
			return "HD"
		elif score >= 75 and score < 85:
			return "D"
		elif score >= 65 and score < 75:
			return "C"
		elif score >= 50 and score < 65:
			return "P"
		else:
			return "F"

user_input = input("Please enter the students serial number...\n")
try:
	int(user_input.strip()) #Assuming serial nos are pure int
except:
	print("Please enter a value!\n")
else:
	scoreinput = input("Now, please enter the score of the student \n")
	try:
		float(scoreinput)
	except:
		print("Please enter a numerical value!\n")
	else:
		print ("You entered a score of "+scoreinput+"\n")
		print ("The calculated grade is "+str(examscore().calcgrade(scoreinput)))