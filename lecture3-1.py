x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)
	

	def vowel(s):
    count = 0
    for i in s.lower():
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count