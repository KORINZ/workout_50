#converting English word to Pig Latin.

def pig_latin():

	word = input('Enter an English word to covert into Pig Latin: ').lower()
	
	starting_vowel = False

	for vowel in 'aeiou':
		if word[0] == vowel:
			word += 'way'
			starting_vowel = True
			break

	if starting_vowel == False:
		word = list(word)
		word.append(word[0])
		word.append('ay')
		word.remove(word[0])
		word = ''.join(word)

	return print(word)

pig_latin()

"""
def pig_latin(word):
	if word[0] in 'aeiou':
		return f'{word}way'
	return f'{word[1:]}{word[0]}ay'
	
print(pig_latin('python'))
"""