def McNuggets(n):
	"""
	n is an int

	Returns True if some integer combination of 6, 9 and 20 equals n
	Otherwise returns False.
	"""
	# Your Code Here
	for a in range(n/6):
		for b in range(n/9):
			c = n - 6a - 9b
			if c >= 0 and c % 20 == 0:
				return True
	return False
		