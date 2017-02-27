# def oddTuples(aTup):
#     '''
#     aTup: a tuple
#
#     returns: tuple, every other element of aTup.
#     '''
    # Your Code Here
# aTup=('I', 'am', 'a', 'test', 'tuple')
# print(aTup[0::2])
#

# x = [1, 2, [3, 'John', 4], 'Hi']
# x[0] = 8
# print(x)

# listA = [1, 4, 3, 0]
# listB = ['x', 'z', 't', 'q']
# print(listA.sort)
# print(listA.sort())
# print(listA)
# print(listA.insert(0,100))
# print(listA.remove(3))
# print(listA.append(7))
# print(listA)
# print(listA+listB)
# print(listB.sort())
# print(listB.pop())
# print(listB.count('a'))
# print(listA.extend([4, 1, 6, 3, 4]))
# print(listA.count(4))
# print(listA.index(1))
# print(listA.pop(4))
# print(listA.reverse())
# print(listA)

# --------------exercice aply to each--------------------------
testList = [1, -4, 8, -9]

# def applyToEach(testList, abs):
#     for i in range(len(testList)):
#         testList[i] = abs(testList[i])
#     return testList
#
#
# print(applyToEach(testList, abs))




#
# def applyToEach(testList):
#     for i in range(1,len(testList)):
#             testList[i] = testList[i]*testList[i]
#     return testList
#
#
# print(applyToEach(testList))


#------------------exercice 5-----------------------------------
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1


print(applyEachTo([inc, square, halve, abs], -3))
print(applyEachTo([inc, square, halve, abs], 3.0))
print(applyEachTo([inc, max, int], -3))
