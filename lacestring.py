def laceStrings(s1, s2):
	"""
	s1 and s2 are strings.

	Returns a new str with elements of s1 and s2 interlaced,
	beginning with s1. If strings are not of same length, 
	then the extra elements should appear at the end.
	"""
	s = ''
	L1 = len(s1)
	L2 = len(s2) 
	if s1 == '':
		s = s2
	elif s2 == '':
		s = s1
	elif L1 > L2:
		for i in range(L2):
			s = s + s1[i] + s2[i]
		s = s + s1[L2: L1]
	elif L1 < L2:
		for j in range(L1):
			s = s + s1[j] + s2[j]
		s = s + s2[L1: L2]	
	else:
		print "error"
	
	return s
print laceStrings('abcd', 'efghi')
print laceStrings('', 'abc')
print laceStrings('', '')
print laceStrings('abc', '')
print laceStrings('abcdefgh', 'ijk')
