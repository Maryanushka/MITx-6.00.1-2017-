def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

print(linearSearch([21, 1, 25, 22, 30, 13, 7, 24, 12], 24))
