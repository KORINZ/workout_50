#reimplementing sum() functionality in Python.

def mysum(*numbers):

	sum_result = 0

	for number in numbers:
		sum_result += number
	return sum_result

print(mysum(3,33,333))