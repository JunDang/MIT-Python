def AlphaSubstrings(s):
	s = s.lower()
	i = 0
	longest = ''
	for j in range(1, len(s)):
		if s[j-1] > s[j]:
			if len(longest) < j - i:
				longest = s[i:j]
			i = j
	if len(s[i:]) > len(longest):
		longest = s[i:]
	return longest
#print AlphaSubstrings('wkxbkkwdbc')
print len('hosazzttsdmalzz')
print AlphaSubstrings('hosazzttsdmalzza')
