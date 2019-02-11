import random
import re
with open("unipi.txt", 'r') as f:
	lines = f.readlines()
	table = []
	string = " "
	i = 0
	for line in lines:
		for word in re.findall(r'\w+', line):
			i = i + 1
			string = string + " " + word 

			if (i == 3) :
				table.append(string)
				i = i + 1

			if (i == 4) :
				string = " "
				i = 0	
		
	random.shuffle(table)
	with open("newunipii.txt", 'w') as f:
		for t in table:
			f.write (t)
			
		