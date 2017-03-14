# 20.0 points possible (graded)
# You are given the following definitions:
#
# A run of monotonically increasing numbers means that a number at position k+1 in the sequence is greater than or equal to the number at position k in the sequence.
# A run of monotonically decreasing numbers means that a number at position k+1 in the sequence is less than or equal to the number at position k in the sequence.
# For example:
#
# If L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] then the longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7] and the longest run of monotonically decreasing numbers in L is [10, 4, 3]. Your function should return the value 26 because the longest run of monotonically increasing integers is longer than the longest run of monotonically decreasing numbers.
# If L = [5, 4, 10] then the longest run of monotonically increasing numbers in L is [4, 10] and the longest run of monotonically decreasing numbers in L is [5, 4]. Your function should return the value 9 because the longest run of monotonically decreasing integers occurs before the longest run of monotonically increasing numbers.



def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """


    # последовательность повозрастанию
    maximum_inc = []
    inc = []
    for i in range(len(L)-1):
        if L[i]>= L[i-1] :
            inc.append(L[i-1])
            inc.append(L[i])
            if len(maximum_inc) < len(inc):
                maximum_inc = inc
        else:
            inc = []


    increasent_sub = maximum_inc[::2]+maximum_inc[len(maximum_inc)-1:]


    # последовательность поубыванию
    dec = []
    maximum_dec = []
    for i in range(len(L) - 1):
        if L[i] <= L[i-1]:
            dec.append(L[i-1])
            dec.append(L[i])
            if len(maximum_dec) < len(dec):
                maximum_dec = dec
        else:
            dec = []

    decreasent_sub= maximum_dec[::2]+maximum_dec[len(maximum_dec)-1:]

    index_dec = L.index(decreasent_sub[0])
    index_inc = L.index(increasent_sub[0])

    # вычисляем какой кусок длиннее
    if len(increasent_sub) > len(decreasent_sub):
        return sum(increasent_sub)
    elif len(increasent_sub) < len(decreasent_sub):
        return sum(decreasent_sub)
    elif len(increasent_sub) == len(decreasent_sub):
        if index_dec > index_inc:
            return sum(decreasent_sub)
        else:
            return sum(increasent_sub)





print(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))