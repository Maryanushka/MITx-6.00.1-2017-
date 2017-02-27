# # 7
# # d1 = {1: 30, 2: 20, 3: 30}
# # d2 = {1: 40, 2: 50, 3: 60}
# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# sym_diff = d1.keys() ^ d2
# intersect = d1.keys() & d2
# print(sym_diff)
# print(intersect)
#
# # if d1.keys() == d2.keys():
# #     d = {a + 1: False for a in range(len(d1))}
# #     t = ()
# #     t = d, {}
# #     print(t)
# # else:
# #     t = ()
# #     d = {k: d1.get(k,0) + d2.get(k,0) for k in set(d1) & set(d2)}
#
#
#
# def f(a,b):
#     return a > b
#
# def dict_interdiff(d1, d2):
#     '''
#     d1, d2: dicts whose keys and values are integers
#     Returns a tuple of dictionaries according to the instructions above
#     '''
#     # Your code here
#     if f(d1.keys(), d2.keys()) == True:
#         # intersection, keys that are common to both d1 and d2.
#         l = [d1[k] for k in d1.keys() if not k in d2]
#         d = {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) & set(d2)}
#         t = ()
#         t = d
#         return t
#     elif f(d1.keys(), d2.keys()) == False:
#         d = {a + 1: False for a in range(len(d1))}
#         t = ()
#         t = d, {}
#         return t
#
#     # apply f on values of the keys that common to both dicts.
#     # a = {k: f(d1[k], d2[k]) for k in intersect}
#     # b = {k: d1[k] for k in sym_diff & d1.keys()}
#     # add key/value pairings from d2 using keys that appear in sym_diff
#     # b.update({k: d2[k] for k in sym_diff & d2.keys()})
#     # return a, b
# print(dict_interdiff({1:30, 2:20, 3:30 },{1:40, 2:50, 3:60}))


# Problem 7
# 20/20 points (graded)
# Assume you are given two dictionaries d1 and d2, each with integer keys and integer values. You are also given a function f, that takes
# in two integers, performs an unknown operation on them, and returns a value.

# Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). The function will return a tuple of two
# dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, calculated as follows:
# intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect
# dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- the value of the common key in d1 is
# the first parameter to the function and the value of the common key in d2 is the second parameter to the function. Do not implement f
# inside your dict_interdiff code -- assume it is defined outside.
# difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2
# or (b) every key-value pair in d2 whose key appears only in d2 and not in d1.

# Here are two examples:
# If f(a, b) returns a + b
# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
# If f(a, b) returns a > b
# d1 = {1:30, 2:20, 3:30}
# d2 = {1:40, 2:50, 3:60}
# then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})

# def dict_interdiff(d1, d2):
#    '''
#    d1, d2: dicts whose keys and values are integers
#    Returns a tuple of dictionaries according to the instructions above
#    '''
#    # Your code here



# Paste your function here
def dict_interdiff(d1, d2):
    intersect = {}
    difference = {}
    for key in d1.keys():
        if key in d2.keys():
            intersect[key] = f(d1[key], d2[key])
        else:
            difference[key] = d1[key]
    for key in d2.keys():
        if key not in d1.keys():
            difference[key] = d2[key]
    return (intersect, difference)


def f (a,b):
    return a > b

