#!/usr/bin/env python3
#
#	Python3 script to write headers for java CSCI213.
#	
#	DO NOT ATTEMPT TO USE THIS ON A WINDOWS COMPUTER!
#
#	No support provided
#	BACK UP YOUR FILES BEFORE USING
#	NOT RESPONSIBLE FOR ANY FUCKUPS.
#	@author Jingkai.
#	If you need help with arguments please use --help
#	If you still need help after that you probably shouldn't be scripting your headers.
#	Adopted from derlin and modified.
#	usage python3 add_headers.py --name <yourname> --uow <studentid> --ano <assignment number>


# argument parser.
import argparse
# because of indentations being captured..
import textwrap

import os

accepted_files="java"

def print_header(message):
	print("===========================")
	print(message)
	print("===========================")

def list_all_files():
	list_of_file=[]
	for root, directories, filenames in os.walk('.'):
		for filename in filenames: 
			if is_accepted(filename):
				list_of_file.append(os.path.join(root,filename))
	return list_of_file

def is_accepted(filename):
	return True if filename.endswith(accepted_files) else False

def check_for_headers(file_list):
	list_of_no_header = []
	for f in file_list:
		if not has_header(f):
			list_of_no_header.append(f)
	return list_of_no_header

def has_header(filename):
	with open(filename) as reader:
		lines = reader.read().lstrip().splitlines()
		if len(lines) > 0:
			return True if lines[0].startswith("/*") else False
		else:
			return False

def write_header(filename,header):
	with open(filename, 'r') as f:
		temp = f.read()
	file = filename.split('/')[-1]
	replaced_name = header.replace("filenamegarbage",file)
	desc = input("Enter a description for {}: ".format(file))
	replaced_desc = replaced_name.replace("descriptiongarbage",desc)
	print(replaced_desc)

	with open(filename,'w') as fw:
		fw.write(replaced_desc+temp)
	print("{} header written".format(file))

def check_args(args):
	if not args.name:
		print("A name is required! (for more --help)")
		exit()

	if not args.uow:
		print("A uow student id is required (for more --help)")
		exit()

	if not args.ano:
		print("Assignment no is required, (for more --help)")
		exit()

	try:
		sid = int(args.uow)
	except ValueError:
		print("Only integers are accepted")
		exit()

	try:
		ano = int(args.ano)
	except ValueError:
		print("Only integers are accepted")
		exit()


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--name', help='Enter your name')
	parser.add_argument('--uow', help='Enter your studentID')
	parser.add_argument('--ano', help='Enter your assignment No')
	args = parser.parse_args()
	check_args(args)
	template_string = textwrap.dedent("""/*
*	CSCI213 Assignment {}
*-------------------------------
*	File name: {}
*	Author:{}
*	Student Number:{}
*	Description:{}
*/\n""").format(str(args.ano),"filenamegarbage",
		args.name,str(args.uow),"descriptiongarbage")

	print_header("Sample Template")
	print(template_string)
	print_header("Seeking Java Files")
	list_of_found_files = list_all_files()
	if len(list_of_found_files) == 0:
		print("No java files found")
		exit()
	else:
		print(*list_of_found_files,sep='\n')
	print_header("Seeking java files with no headers")
	list_of_headless_files =check_for_headers(list_of_found_files)
	if len(list_of_headless_files) == 0:
		print ("No files need headers")
		exit()
	else:
		print(*list_of_headless_files,sep='\n')
	while(True):
		sel = input("We will now proceed with writing.(Y/N): ")
		if sel == 'Y':
			break
		elif sel == 'N':
			print("Exiting")
			exit()
		else:
			print("Unrecognized")
	for file in list_of_headless_files:
		write_header(file,template_string)
	
	print_header("All files written, goodbye!")
