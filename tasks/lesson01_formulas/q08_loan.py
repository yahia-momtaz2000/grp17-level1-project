# solve the loan equation
import math

# inputs
loan_amount = 100_000
monthly_interest_rate = 0.01
no_years = 7

# Solving Monthly payment
denominator_result = 1 / ( math.pow(1 + monthly_interest_rate, no_years * 12))

monthly_payment = loan_amount * monthly_interest_rate / (1 - denominator_result)
monthly_payment = round(monthly_payment, 2)
print('Monthly payment = ',monthly_payment)

# solve total payment
total_payment = monthly_payment * no_years * 12
print('Total payment = ', total_payment)
