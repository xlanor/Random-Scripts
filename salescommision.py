#! /usr/bin/env python3
#-*- coding: utf-8 -*-
##
# commision script
# Written by xlanor
# to help someone with homework.
##
## This script assumes that you are using the sample foo.xls
## No validation is done in this script.
## run in terminal.

import xlrd

class salescommision():
	def importxlx(self,name):
		workbook = xlrd.open_workbook(name+'.xls')
		workbook = xlrd.open_workbook(name+'.xls', on_demand = True)
		worksheet = workbook.sheet_by_index(0)
		first_row = [] # The row where we stock the name of the column
		for col in range(worksheet.ncols):
		    first_row.append( worksheet.cell_value(0,col) )
		# transform the workbook to a list of dictionaries
		data =[]
		for row in range(1, worksheet.nrows):
		    elm = {}
		    for col in range(worksheet.ncols):
		        elm[first_row[col]]=worksheet.cell_value(row,col)
		    data.append(elm)
		return(data)

	def printdetails(self,xlxname):
		salesdict = self.importxlx(xlxname)
		details = []
		for each in salesdict:
			commission = self.calcomission(each['Retail_Price'],each['Transaction_Code'])
			details.append({"retail_price":each['Retail_Price'],"commission":commission,"employee_no":each['Employee_No']})
		return details
	def calcomission(self,price,grade):
		if grade == "A":
			return float(price) * 0.06
		elif grade == "B":
			return float(price) * 0.08
		else:
			return float(price) * 0.1

user_input = input("Please enter the workbook's name (if foo.xls please key in foo)...\n")
try:
detailsdict = salescommision().printdetails(user_input)
print(detailsdict)
for each in detailsdict:
	print("Employee No: "+str(each['employee_no'])+"\n")
	print("Retail Price: "+str(each['retail_price'])+"\n")
	print("Commision: "+str(each['commission'])+"\n")
	print("--------------------------------------\n")
except:
	print("Oh noes something happened")