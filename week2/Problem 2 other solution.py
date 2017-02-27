# ----------------------------another solution------------------------
# PROBLEM 2: PAYING DEBT OFF IN A YEAR  (15 points possible)
# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within
# 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant
# amount that will be paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:

# balance = 3329
#
# annualInterestRate = 0.2
#
# # The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
#
# lowestPayment = 0
# finding = True
#
#
# def payment(balance, annualInterestRate, lowestPayment):
#     month = 1
#     while month <= 12:
#
#         # Monthly interest rate= (Annual interest rate) / 12.0
#         monthlyIntRate = annualInterestRate / 12.0
#
#         # Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#         balance -= lowestPayment
#
#         # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#         balance += (monthlyIntRate * balance)
#
#         month += 1
#
#         if balance <= 0:
#             return lowestPayment
#     else:
#         return False
#
#
# while finding == True:
#     if payment(balance, annualInterestRate, lowestPayment):
#         finding = False
#         print
#         'Lowest Payment:', payment(balance, annualInterestRate, lowestPayment)
#     else:
#         lowestPayment += 10
#         payment(balance, annualInterestRate, lowestPayment)
# ------------------another solution--------------------------------