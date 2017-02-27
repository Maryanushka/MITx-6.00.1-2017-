# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1




# iteration = 0
# count = 0
# while iteration < 5:
#
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1





# def fourPower(x):
#     '''
#
#     :param x:
#     :return: int or float
#     '''
#     def square(x):
#         return x*x
#     print(square(square(x)))
#
# fourPower(4)






# def odd(x):
#     '''
#
#     :param x:
#     :return: boolean true or false
#     '''
#     y = x%2!=0
#     print(y)
# odd(-38)






# def iterPower(base, exp):
#     '''
#
#     :param base: int or float
#     :param exp: int >=0
#     :return: int or float base^exp
#     '''
#
#     result=1
#     while exp >=1:
#             result *= base
#             exp -= 1
#     print("%.4f" % result)
#
# iterPower(-3.27, 3)

# def recurPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#
#     returns: int or float, base^exp
#     '''
    # if exp == 0 :
    #     return 1
    # return base * recurPower(base, exp-1)
#
#     if exp == 0:
#         print(1)
#     elif exp ==1:
#         print("%.4f" % base)
#     else:
#         return base * recurPower(base, exp-1)
# recurPower(1.12, 3)










