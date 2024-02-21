# Write a Python function that takes a list of strings as input and 
# returns a new list containing only the strings with more than 5 characters.

def greater_than_five(string_list):
	new_list = []
	for string in string_list:
		if len(string) > 5:
			new_list.append(string)
	return new_list