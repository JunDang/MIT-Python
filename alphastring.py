def AlphaSubstrings(s):
longest =''
current = ''
start = 0
#end = 1
for end in range (1, len(s)):
	if s[end] < s[end - 1]: 
	#decline starts. It means from start to end - 1 is always increasing. 
	#s[start: end] is the substring required. The length is end -start
		if (len(current) > len(longest)):
			longest = current
		current = ''
	else:
		#It is still increasing. Do nothing. 
		if len(current) == 0:
			current = current + s[end-1: end + 1]
		else:
			current = current + s[end]
if (len(current) > len(longest)):
	longest = current
return longest
print AlphaSubstrings('abcdefghijklmnopqrstuvwxyz')
print AlphaSubstrings('ntrhworwfkxytxrqw')
print AlphaSubstrings('znrtkizoscpumqocmggynm')
print AlphaSubstrings('rjpalhvngghvct')