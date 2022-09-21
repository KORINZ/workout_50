#number guessing game (an integer number from 1 to 100).

import random

def guessing_game():
	number = random.randint(1, 100)

	user_answer = int(input('What integer number (from 1 to 100) has been chosen? '))
	
	while user_answer != number:
		if user_answer > number:
			user_answer = int(input(f'{user_answer} is too high! Choose again: '))
		else:
			user_answer = int(input(f'{user_answer} is too low! Choose again: '))
	
	return print(f'{user_answer} is just right!')

guessing_game()