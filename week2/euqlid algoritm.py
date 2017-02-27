def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b



#     recursive solution
#     if b==0:
#         return a
#     else:
#         return gcdRecur(b,a%b)

print(gcdIter(17, 12))