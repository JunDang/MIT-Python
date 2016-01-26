def myLog(x, b):
	power = 0
	value = 1
	while value < x:
		power = power + 1
		value = b**power
	return power
print myLog(9, 3)