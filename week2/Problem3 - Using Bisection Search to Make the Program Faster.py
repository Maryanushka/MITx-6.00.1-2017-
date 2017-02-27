# In short:
#
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
#
# Write a program that uses these bounds and bisection search
# (for more info check out the Wikipedia page on bisection search)
# to find the smallest monthly payment to the cent (no more multiples of $10)
# such that we can pay off the debt within a year.
# Try it out with large inputs, and notice how fast it is
# (try the same large inputs in your solution to Problem 2 to compare!).
# Produce the same return value as you did in Problem 2.



balance = 320000
annualInterestRate = 0.2
air = (annualInterestRate/12.0)+1
lower = balance / 12.0
upper = (balance * ((annualInterestRate/12.0) + 1)**12.0) / 12.0
tempBal = balance
minPay = (lower + upper) / 2.0 # it's a middle element for bisec search

while abs(tempBal) > 1:
    tempBal= balance
    for i in range(0,12):
        tempBal = (tempBal - minPay) * air
    if tempBal < 0:
        upper = minPay
    else:
        lower = minPay
    minPay = (lower + upper) / 2.0
print(round(minPay,2))






