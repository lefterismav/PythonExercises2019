def MaxDistance (list,x):
	sum = 0
	for i in list:
		sum = sum + i
		if sum > x :
			sum = sum - i
	print("The greatest sum of the list that does not overreach the given attribute is",sum)
	
MaxDistance([1,3,5,5,2],7)
