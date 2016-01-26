'''
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

def CreditCard(balance, annualInterestRate, monthlyPaymentRate):
	MonthlyInterestRate = annualInterestRate / 12.0
	totalPaid = 0
	for i in range(1, 13): 
		MinimumMonthlyPayment = monthlyPaymentRate * balance
		monthlyUnpaidBalance = balance - MinimumMonthlyPayment
		balance = monthlyUnpaidBalance + MonthlyInterestRate * monthlyUnpaidBalance
		totalPaid = totalPaid + MinimumMonthlyPayment 
		print "Month: " + str(i)
		print "Minimum monthly payment: " + str("%.2f" % MinimumMonthlyPayment)
		print "Remaining balance: " + str("%.2f" % balance)
	print "Total paid: " + str("%.2f" % totalPaid)
	print "Remaining balance: " + str("%.2f" % balance)
CreditCard(4213, 0.2, 0.04)
