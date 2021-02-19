secret_number = 8
guess_count = 0
guess_limit = 3
guess_remain = 3

print('Guess From These Numbers: 5, 2, 8, 6, 5, 10')

while guess_count < guess_limit:
	guess = int(input('Guess the number: '))
	guess_count += 1
	guess_remain -= 1
	
	if guess == secret_number:
		print('Congratulations! You Win The Game!')
		break
	elif guess_remain == 0:
		print('Guess Limit Exceed!')
	else:
		print('Try Again. You have remaining ' + f'{guess_remain} guess')
else:
	print('Game Over....')