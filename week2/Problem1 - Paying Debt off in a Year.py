# def payingDebt(balance, annualInterestRate, monthlyPaymentRate):
#     '''
#     Monthly interest rate= (Annual interest rate) / 12.0
#     Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#     Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#     Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#     '''
#     m = 0   # where m is month
#     s = "Remainding balance: "
#     air = annualInterestRate/12
#
#     while m < 12:
#         minPay = monthlyPaymentRate * balance
#         balance -= minPay
#         balance += air*balance
#         m+=1
#     return '{}{}'.format(s,round(balance,2))
#
#
# print(payingDebt(42,0.2,0.04))



balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
m = 0   # where m is month

air = annualInterestRate/12
s = "Remainding balance: "
while m < 12:
    minPay = monthlyPaymentRate * balance
    balance -= minPay
    balance += air*balance
    m += 1
print('{}{}'.format(s,round(balance,2)))

for month in range(12):
    minPay = monthlyPaymentRate * balance
    balance -= minPay
    balance += air * balance
print('{}{}'.format(s, round(balance, 2)))