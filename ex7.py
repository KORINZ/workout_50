#

def ubbi_dubbi(word):

	output = []

	for letter in word:
		if letter in 'aeiou':
			output.append(f'ub{letter}')
		else:
			output.append(letter)

	return print(''.join(output))



"""
def ubbi_dubbi(string):

	ub_word = []

	for letter in list(string.lower()):
		if letter in 'aeiou':
			letter = 'ub' + letter
		ub_word += letter

	return print(''.join(ub_word))
"""
ubbi_dubbi('hello')
