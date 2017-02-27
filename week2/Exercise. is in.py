def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    middle= len(aStr)//2
    if aStr == "":
        return False
    elif aStr == 1:
        return False
    elif char == aStr[middle]:
        return True
    else:
        if char < aStr[middle]:
            return isIn(char, aStr[:middle])
        else:
            return isIn(char, aStr[middle+1:])


print(isIn('n', 'bz'))

