'''
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12.0
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
'''

def CreditCard(balance, annualInterestRate):
MonthlyInterestRate = annualInterestRate / 12.0
low = balance / 12.0
high = (balance * (1 + MonthlyInterestRate)**12) / 12.0
monthlyPayment = (low + high) / 2
	
while True:
	currentbalance = balance
	monthlyPayment = (low + high) / 2
	for i in range(1, 13):
		currentbalance = (currentbalance - monthlyPayment) * (1 + MonthlyInterestRate)
	if currentbalance > 0.01:
		low = monthlyPayment
	elif currentbalance < -0.01:
		high = monthlyPayment
	else:
		break
	
print ("%.2f" % monthlyPayment)
CreditCard(320000, 0.2)	
CreditCard(999999, 0.18)
			