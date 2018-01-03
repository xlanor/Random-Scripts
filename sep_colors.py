#! /usr/bin/env python3
#-*- coding: utf-8 -*-
##
# Counts the number of excel cells
##
import xlrd


class handleWorkbook():
	def __init__(self):
		self.red = [(153,51 ,0)]
		self.blue = [(0, 128, 128)]

	def import_worksheet(self,filename):
		book = xlrd.open_workbook(filename,formatting_info = True)
		sheets = book.sheet_names()
		for index, sh in enumerate(sheets):
			col_dict = {}
			sheet = book.sheet_by_index(index)
			rows, cols = sheet.nrows, sheet.ncols
			for row in range(rows):
				red_counter = 0
				blue_counter = 0
				row_array = {}
				for col in range(cols):
					# could get 'dump', 'value', 'xf_index'
					xfx = sheet.cell_xf_index(row, col)
					xf = book.xf_list[xfx]
					bgx = xf.background.background_colour_index
					bgx = self.get_color(book,bgx)
					new_col = col+1
					if bgx in self.red:
						if new_col in col_dict:
							if "blue" in col_dict[new_col]:
								col_dict[new_col]["red"] += 1
							else:
								col_dict[new_col]["red"] = 1
						else:
							col_dict[new_col] = {}
							col_dict[new_col]["red"] = 1
					if bgx in self.blue:
						if new_col in col_dict:
							if "blue" in col_dict[new_col]:
								col_dict[new_col]["blue"] += 1
							else:
								col_dict[new_col]["blue"] = 1
						else:
							col_dict[new_col] = {}
							col_dict[new_col]["blue"] = 1

			

			self.print_col_dict(col_dict)
			self.print_summation(col_dict)

	def get_color(self,book,color_index):
		return book.colour_map.get(color_index)

	def print_summation(self,col_dict):
		red_only_count = 0
		both_count = 0
		for key,value in col_dict.items():
			try:
				blue = value["blue"]
			except KeyError:
				red_only_count += 1
			else:
				both_count += 1
		print("A total of "+str(red_only_count)+" columns has red cells only")
		print ("A total of "+str(both_count)+" columns have both cells")
		
	def print_col_dict(self,col_dict):
		for key,value in col_dict.items():
			try:
				red = value["red"]
			except KeyError:
				red = 0
			try:
				blue = value["blue"]
			except KeyError:
				blue = 0
			print(str(key) + " has " +str(red)+" red and "+str(blue)+" blue cells")




if __name__ == "__main__":
	handleWorkbook().import_worksheet("jayfriend.xls")