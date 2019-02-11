with open("add2numbers.txt", 'r') as f:
    lines = f.readlines()

with open("newadd2numbers.txt", 'w') as f:
	for line in lines:
        	
		if line[0:2] == "#!":
			f.writelines(line)
			print(line)
		
		elif not line.strip():
			f.writelines(line)
			print(line)
		
		else:
			line = line.split('#')
			stripped_string = line[0].rstrip()
			
			if stripped_string:
				f.writelines(stripped_string)
				f.writelines('\n')
				print(line)
	
		