# mortgage.py
#
# Exercise 1.7
principle = float(input("How much principle do you have: "))
rate = float(input("What is your interest rate: ")) / 100
payment = 2684.11
total_paid = 0.0
months = 0

additional_payment = 1000.0
additional_payment_start = 0
additional_payment_end = 12

while principle > 0:
    months += 1
    principle = principle * (1+rate/12) - payment
    total_paid = total_paid + payment

    if months >= additional_payment_start and months <= additional_payment_end:
        principle -= additional_payment
        total_paid += additional_payment

    print(months, round(total_paid, 2), round(principle, 2))


print('Total Paid: ', round(total_paid, 2), 'Total Months: ', months)
