import re
table = []
def max_char_count(str):
	max_char = ''
	max_count = 0
	min_count = 100
	min_char = ''
	for char in set(str):
		count = string.count(char)
		if count > max_count:
			max_count = count
			max_char = char	
		if count < min_count:
			min_count = count
			min_char = char
			
	print ("The character appears the most is: ",max_char)
	print ("The character appears the least is: ",min_char)
	table.append(max_char)
	table.append(min_char)
	return max_char, min_char;
			

with open("unipi.txt", 'r') as f:
	lines = f.readlines()
	string = ""
	string2 = ""

	
	
	for line in lines:
		for word in re.findall(r'\w+', line):
			string2 = string2 + ' ' + word
			string = string + word
	max_char_count(string)
	list_of_letters = list(string2.lstrip())
	
	for i in range(len(list_of_letters)):
		if(list_of_letters[i] == table[0]):
			list_of_letters[i] = table[1].upper()
		elif(list_of_letters[i] == table[1]):
			list_of_letters[i] = table[0].upper()

	str = ''.join(list_of_letters)
	print (str)









