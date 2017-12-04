#! /usr/bin/env python3
#-*- coding: utf-8 -*-
##
# Written by xlanor
# to help someone with homework.
##

class Homework():
	def input_air1(self):
		air1 = input("Please enter Air1\n")
		return air1
	def input_air2(self):
		air2 = input("Please enter Air2\n")
		return air2
	def sort_investment(self,investment):
		#selection sort implementation
		for i in range(len(investment)):
			least = i #assume investment[i] lowest
			for k in range(i+1, len(investment)): #look at the rest of the list
				if investment[k] < investment[least]: #if theres any lower, do a swap.
					least = k
			tmp = investment[least]
			investment[least] = investment[i]
			investment[i] = tmp
		return investment


	def calculate_investment(self,investment,air1,air2):
		calculated_investment = []
		for i in investment:
			if i > 5000:
				air = air1
			else:
				air = air2
			#assuming that calculation of investment means that.
			# if air1 is 7%, means you must pay 7% of the value?

			calculated_investment.append((i/100)*float(air))
		return calculated_investment

	def print_all(self,investment):
		air1 = self.input_air1()
		air2 = self.input_air2()
		print ("Original investment: ")
		[print(x) for x in investment]
		print ("Sorted investment: ")
		sorted_investment = self.sort_investment(investment)
		[print(s) for s in sorted_investment]
		print ("Calculated investment: ")
		calculated_investment = self.calculate_investment(investment,air1,air2)
		[print(calculated) for calculated in calculated_investment]


if __name__ == "__main__":
	investment = [2000,8000,6000,4000,7000]
	Homework().print_all(investment)
