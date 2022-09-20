# sorting the letters inside an immutable string from the lowest Unicode value to the highest Unicode value.

def strsort(string):

	string_list = list(string.lower())
	string_list.sort()
	string_sorted = string_list

	return print(''.join(string_sorted))

strsort('qwertyuiopasdfghjklzxcvbnm')