with open("add2numbers.txt", 'r') as f:
    lines = f.readlines()

with open("newadd2numbers.txt", 'w') as f:
	for line in lines:
        	# Keep the line
		if line[0:2] == "#!":
			f.writelines(line)
			print(line)
		# Keep existing empty lines
		elif not line.strip():
			f.writelines(line)
			print(line)
		# Remove comments from other lines
		else:
			line = line.split('#')
			stripped_string = line[0].rstrip()
			# Write the line only if the comment was after the code.
			# Discard lines that only contain comments.
			if stripped_string:
				f.writelines(stripped_string)
				f.writelines('\n')
				print(line)
	
		