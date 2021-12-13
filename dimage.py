import csv
import os

with open('honor.csv', 'r') as file:
	csvreader = csv.reader(file)
	header = next(csvreader)
	for row in csvreader:
		images = row[1].split(' , ')
		for img in images:
			os.system('wget ' + img + ' $');