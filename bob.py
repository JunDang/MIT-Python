def bob(s):
	count = 0
	for i in s.inex():
		if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
			count += 1
	return count