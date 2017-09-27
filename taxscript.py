#! /usr/bin/env python3
#-*- coding: utf-8 -*-
##
# Income Tax Script.
# Written by xlanor
# Based on values provided by IRAS site as of 170928
##

class Incometax():
	def incometax(self,income):
		income = float(income) #converting to float in case its passed as a string
		if income <= 20000:
			return 0 #no taxes woohoo ah gong give rebate!

		elif income > 20000 and income < 30000: #else if income greater than equals to, but less than 30k
			return self.calculations(income,20000,0.02,200)
			
		elif income >= 30000 and income < 40000:  
			return self.calculations(income,30000,0.035,550)

		elif income >= 40000 and income < 80000:
			return self.calculations(income,40000,0.07,3350)

		elif income >= 80000 and income < 120000:
			return self.calculations(income,80000,0.115,7950)
		elif income >= 120000 and income < 160000:
			return self.calculations(income,120000,0.15,13950)

		elif income >= 160000 and income < 200000:
			return self.calculations(income,160000,0.17,20750)

		elif income >= 200000 and income < 320000:
			return self.calculations(income,200000,0.18,42410)

		elif income >= 320000:
			return self.calculations(income,320000,0.2,42350)

	def calculations(self, income, tier, percent, gross):
		taxable_income = income - float(tier)
		payable_percent = taxable_income * float(percent)
		total_payable = payable_percent + float(gross)
		return total_payable

user_input = input("Please enter your income...\n")
try:
	float(user_input)
except:
	print("Please enter a numerical value!\n")
else:
	print ("You entered a value of $"+user_input+"\n")
	print ("Your calculated payable tax is $"+str(round(Incometax().incometax(user_input),2)))

		