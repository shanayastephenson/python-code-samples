# This function even_numbers_only iterates through each number in the input list 
# and checks if it's even (i.e., divisible by 2 with no remainder). 
# If so, it appends the number to the even_numbers list. 
# Finally, it returns the list containing only the even numbers.

def even_numbers_only(number_list):
	even_number_list=[]
	for num in number_list:
		if num % 2 == 0:
			even_number_list.append(num)
	return even_number_list
	
