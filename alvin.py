#! /usr/bin/env python3
import os, os.path
import traceback
import contextlib
import math
import csv
class getItems():
	def get_dat(self):
		items = os.listdir(".")
		items_removed = []
		for x in items:
			# because there are some hidden folders that will be grabbed
			# as well as this script,
			# we check the first 2 letters of all directories grabbed if
			# it starts with mu and construct a new list to put them into.
			if x[:2] == "mu":
				items_removed.append(int(x[3:]))
 
		items_removed = sorted(items_removed)
		for index,truncated in enumerate(items_removed):
			items_removed[index] = "mu="+str(truncated)

		#gets a list of all directories
		pwd = os.getcwd() #your current working drive
		return_list = []
		for each in items_removed:
			# /Users/Alvin/Desktop/cy2001 results/varymuwhenv=5/mu=30/uni.dat
			#each = subfolder.
			#{ subfolder | mean |  sd }
			individual_dir = pwd+'/'+each+'/uni.dat'
			print(individual_dir)
			dict_to_append = {}
			with open (individual_dir,"r") as datfile:
				rightlist = []
				datfilelist = datfile.read().split()
				counter = 0
				for item in datfilelist:
					if counter%2 : 
						rightlist.append(float(item))
					counter +=1
				# we want to calculate mean here
				mean = self.calculate_mean(rightlist)
				sd = self.standard_deviation(rightlist)
				dict_to_append["subfolder"] = int(each[3:])
				dict_to_append["mean"] = mean
				dict_to_append["sd"] = sd
				return_list.append(dict_to_append)

		self.construct_csv(return_list,pwd)

	def calculate_mean(self,array_of_items):
		length_array = len(array_of_items)
		sum_of_items = float(0)
		for each in array_of_items:
			sum_of_items += float(each)
		#here we have the combined sum,
		mean = sum_of_items/length_array
		return mean
	def standard_deviation(self,array_of_items):
		#calculate mean, go through all items, for each item.
		#minus mean, square sum it divide 90
		mean = self.calculate_mean(array_of_items)
		for index,value in enumerate(array_of_items):
			value = value-mean
			value *= value
			array_of_items[index] = value
		sum_of_squared = sum(array_of_items)
		divide_of_sum = float(sum_of_squared/90)
		sqrt_of_divided = math.sqrt(divide_of_sum)
		return sqrt_of_divided
	def construct_csv(self,array_of_calculations,pwd):
		csv_List = [["subfolder","mean","Standard Deviation"]]
		for row in array_of_calculations:
			csv_List.append([row['subfolder'],row['mean'],row['sd']])
		csvfile = pwd+'/test.csv'
		with open(csvfile,'w') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerows(csv_List)
			print ("done")
if __name__ == "__main__":
	getItems().get_dat()
