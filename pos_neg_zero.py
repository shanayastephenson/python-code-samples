# This function iterates through each number in the input list and updates the counts accordingly. 
# Finally, it returns a tuple containing the counts of positive numbers, negative numbers, and zeros.

def posnegzero(number_list):
	
	pos_number_count = 0
	neg_number_count = 0
	zero_count = 0
	
	for num in number_list: 
		if num > 0:
			pos_number_count += 1
		elif num < 0: 
			neg_number_count += 1
		else num = 0:
			zero_count += 1
	
	return (pos_number_count,neg_number_count,zero_count)
	

	