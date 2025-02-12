#!/usr/bin/python3

import sys


def text_files():
			#open and read file1 & 2
	with open(file1) as file_one:
		for x in file_one:
			list_one.append(x.strip('\n'))		
	with open(file2) as file_two:
		for y in file_two:
			list_two.append(y.strip('\n'))
	for similar in list_one:
		if similar in list_two:
			similar_list.append(similar)
	# outputting a new text file with matching items
	#removing single quote and creating a new line
	with open('matching_items.txt', 'w+') as similars:
		new = str(similar_list).replace("'", "").replace(",", '\n').replace(" ", "")
		similars.write(new[1:-1])
	for unique in list_two:
		if unique not in list_one:
			unique_list.append(unique)
	#outputting a new text file with non matching items
	#removing single quote and creating a new line
	with open('non_matching.txt', 'w+') as unique:
		improved = str(unique_list).replace("'", "").replace(",", '\n').replace(" ", "")
		unique.write(str(improved[1:-1]))

def csv_files():

	with open(file1) as file_one:
		for x in file_one:
			list_one.append(x.strip('\n'))		
	with open(file2) as file_two:
		for y in file_two:
			list_two.append(y.strip('\n'))
	for similar in list_one:
		if similar in list_two:
			similar_list.append(similar)
	# outputting a new text file with matching items
	#removing single quote and creating a new line
	with open('matching_items.csv', 'w+') as similars:
		new = str(similar_list).replace("'", "").replace(" ", '\n')
		similars.write(new[1:-1])
	for unique in list_two:
		if unique not in list_one:
			unique_list.append(unique)
	#outputting a new text file with non matching items
	#removing single quote and creating a new line
	with open('non_matching.csv', 'w+') as unique:
		improved = str(unique_list).replace("'", "").replace(" ", '\n')
		unique.write(str(improved[1:-1]))

try: 
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	list_one = []
	list_two = []
	similar_list = []
	unique_list = []

	if file1.endswith('.csv') and file2.endswith('.csv'):
		print("Outputting two csv files")
		csv_files()
	elif file1.endswith('.txt') and file2.endswith('.txt'):
		print('Outputting two text files')
		text_files()
	else:
		print('Input csv or txt files only!')
		sys.exit('Exiting....')

except FileNotFoundError:
	print("File does not exist!")
except IndexError:
	print('Enter the two files you would like to compare!')
