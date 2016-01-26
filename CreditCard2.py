'''
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

def CreditCard(balance, annualInterestRate):
	MonthlyInterestRate = annualInterestRate / 12.0
	FixedMonthlyPayment = 0
	for payment in range(10, balance, 10): 
		currentbalance = balance
		for i in range(1, 13):
			#monthlyUnpaidBalance = currentbalance - FixedMonthlyPayment
			#currentbalance = monthlyUnpaidBalance + MonthlyInterestRate * monthlyUnpaidBalance
			currentbalance = (currentbalance - payment) * (1 + MonthlyInterestRate)
			print "Month: " + str(i)
			print "currentbalance: " + str(currentbalance)
			print "payment: " + str(payment)
		if currentbalance < 0:
			FixedMonthlyPayment = payment
			break
	print "-------------------"
	print " Lowest Payment: " + str("%.2f" % FixedMonthlyPayment)
		
CreditCard(3329, 0.2)	
