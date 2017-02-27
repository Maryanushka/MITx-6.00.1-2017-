# Problem 6
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    # Your code here
    g = []
    for i in L:
        g.append(i[::-1])
    L[:] = g[::-1]

