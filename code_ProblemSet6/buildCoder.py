import string
def buildCoder(shift):
	"""
	Returns a dict that can apply a Caesar cipher to a letter.
	The cipher is defined by the shift value. Ignores non-letter characters
	like punctuation, numbers and spaces.

	shift: 0 <= int < 26
	returns: dict
	"""
	upperLetter = string.ascii_uppercase 
	lowerLetter = string.ascii_lowercase 
	dic = {}
	for letter in upperLetter:
		key = letter
		index = upperLetter.index(letter)
		newindex = (index + shift) % 26
		value = upperLetter[newindex]
		dic[key] = value
	for letter in lowerLetter:
		key = letter
		index = lowerLetter.index(letter)
		newindex = (index + shift) % 26
		value = lowerLetter[newindex]
		dic[key] = value
	return dic
print buildCoder(3)