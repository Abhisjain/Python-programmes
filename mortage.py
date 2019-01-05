"""**Mortgage Calculator** - 
Calculate the monthly payments of a fixed term mortgage 
over given Nth terms at a given interest rate. Also figure 
out how long it will take the user to pay back the loan."""

months = int(raw_input("Enter mortgage term (in months): "))
rate = float(raw_input("Enter interest rate: "))
loan = float(raw_input("Enter loan value: "))

monthly_rate = rate / 100 / 12
#formula learn
payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan

print "Monthly payment for a $%.2f %s year mortgage at %.2f%% interest rate is: $%.2f" % (loan, (months / 12), rate, payment)
