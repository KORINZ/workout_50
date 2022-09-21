#taking a hex number and returning the decimal equivalent.

def hex_output():

	decnum = 0
	
	hexnum = input('Enter a hex number to convert to decimal equivalent: ')

	for power, digit in enumerate(reversed(hexnum)):
		decnum += int(digit, 16) * (16 ** power)
	
	#print(power, digit)
	return print(decnum)

hex_output()