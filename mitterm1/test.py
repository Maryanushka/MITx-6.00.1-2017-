# i = 1
# j = 1
#
# while i >=0:
#     while j >= 0:
#         print(i,j)


# stuff = 'iQ'
#
# for t in stuff:
#     if t  == 'iQ':
#         print('ok')

# def square(x):
#     return squareHelper(abs(x), abs(x))
#
# def squareHelper(n,x):
#     if n == 0:
#         return squareHelper(n-1, x)+x
#
# print(squareHelper(8,9))
#

# 5
# a = [1,2,3]
# b = [4,5,6]
#
# def pro(listA,listB):
#     g = [listA * listB for listA , listB in zip(listA, listB)]
#     return sum(g)
#
# print(pro([1,2,3],[4,5,6]))

# 6
# l = [[0,1,2], [1,2,3], [3,2,1], [10,-10,100]]
#
#
# g = [i[::-1] for  i in l]
# print(g[::-1])
# def deep_reverse(L):
#     """ assumes L is a list of lists whose elements are ints
#     Mutates L such that it reverses its elements and also
#     reverses the order of the int elements in every element of L.
#     It does not return anything.
#     """
#     # Your code here
#     # g = [i[::-1] for  i in L]
#     # return g[::-1]
#     g =[]
#     for i in L:
#         g.append(i[::-1])
#     L = g[::-1]
#     return L
#
# print(deep_reverse([[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]))



# 9
# l = [[1, 'a', ['cat'], 2], [[[3], 'dog'], 4,5]]
# def flatten(aList):
#     if aList == []:
#         return aList
#     if isinstance(aList[0], list):
#         return flatten(aList[0]) + flatten(aList[1:])
#     else:
#         return aList[:1] + flatten(aList[1:])
#
# print(flatten([[1, 'a', ['cat'], 2], [[[3], 'dog'], 4,5]]))


# 4
# def closest_power(base, num):
#     '''
#     base: base of the exponential, integer > 1
#     num: number you want to be closest to, integer > 0
#     Find the integer exponent such that base**exponent is closest to num.
#     Note that the base**exponent may be either greater or smaller than num.
#     In case of a tie, return the smaller value.
#     Returns the exponent.
#     '''
#     # Your code here
#     exponent = 0
#     distance = 0
#
#     while True:
#         distance = num - base ** exponent
#         if distance < -20 :
#             exponent -= 1
#             return exponent
#         if distance <= base and distance > -20:
#             return  exponent
#             break
#         exponent += 1
# print(closest_power(11, 66.0))


# 1
# x = "pi"
# y = "pie"
# print(x,y )
# x,y = y,x
# print(x,y)


# def f(x):
#     while x > 3:
#         f(x+1)
# print(f(2))


# i,j =2
# while i >= 0:
#     while j >= 0:
#         print(i, j)

# t = ([1])
# print(type(t))

# def f(x):
#     a = []
#     while x > 0:
#         a.append(x)
#         return a
#     f(x-1)
#
#
# print(f(4))

# s = "12313423423532"
# s1 = ('1', '2','3',)
# s2 = ['1','2','3']
# print(s2[1])
# print(s1[1])
# print(s[1])



# def Square(x):
#     return SquareHelper(abs(x), abs(x))
#
# def SquareHelper(n, x):
#     if n == 0:
#         return 0
#     return SquareHelper(n-1, x) + x
#
# print(Square(3))

# 8

# def f(i):
#     return i + 2
#
#
# def g(i):
#     return i > 5
#
# def applyF_filterG(L, f,g):
#     """
#     Assumes L is a list of integers
#     Assume functions f and g are defined for you.
#     f takes in an integer, applies a function, returns another integer
#     g takes in an integer, applies a Boolean function,
#         returns either True or False
#     Mutates L such that, for each element i originally in L, L contains
#         i if g(f(i)) returns True, and no other elements
#     Returns the largest element in the mutated L or -1 if the list is empty
#     """
#     # Your code here
#     def f(i):
#         return i + 2
#
#     def g(i):
#         return i > 5
#
#     d=[]
#     for i in L:
#         if L == []:
#             return -1
#         elif f(g(i)) == True:
#            d.append(i)
#     return d
#
# print(applyF_filterG([0, -10, 5, 6, -4],))






