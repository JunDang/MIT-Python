low  = 0
high = 100
guess = (low + high ) / 2
print "Please think of a number between " + str(low) + "and " + str(high) + "!"
while True:
	print "Is your secret number " + str(guess) + "?"
	indicator = raw_input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	if indicator == 'h':
		high = (low + high) / 2
	elif indicator == 'l':
		low = (low + high) / 2
	elif indicator == 'c':
		print "Game over. Your secret number was: " + str(guess)
		break
	else: 
		print "Sorry, I did not understand your input."
	guess = (low + high) /2 
