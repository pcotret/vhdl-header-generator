#!/usr/bin/python3
from datetime import datetime
s_filename = input('Filename: ')
s_author = input('Author: ')
s_description = input('Description: ')
s_entity = input('Entity name: ')
s_architecture = input('Architecture name: ')
now = datetime.now()
s_date = now.strftime("%m/%d/%Y")
fin = open("template.vhdt", "rt")
fout = open(s_filename, "wt")
for line in fin:
	line = line.replace('<filename>', s_filename)
	line = line.replace('<author>', s_author)
	line = line.replace('<date>', s_date)
	line = line.replace('<description>', s_description)
	line = line.replace('<entity>', s_entity)
	line = line.replace('<architecture>', s_architecture)
	fout.write(line)
fin.close()
fout.close()