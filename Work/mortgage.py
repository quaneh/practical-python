# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    extra = 0
    if (month >= extra_payment_start_month and month <= extra_payment_end_month):
        extra = extra_payment

    new_principal = principal * (1+rate/12) - (payment + extra)
    if(new_principal < 0):
        total_paid = total_paid + principal
        principal = 0
        print(month, round(total_paid,2), round(principal, 2))
        break

    principal = new_principal

    total_paid = total_paid + (payment + extra)
    month = month + 1
    print(f'Paid ${total_paid:0.2f} over {month} months to decrease the principal to ${principal:0.2f}')
    # print(month, round(total_paid,2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', month)