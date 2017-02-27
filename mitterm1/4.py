# Paste your function here
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    exponent = 0
    distance = 0

    while True:
        distance = num - base ** exponent
        if distance < -20 :
            exponent -= 1
            return exponent
        if distance <= base and distance > -20:
            return  exponent
            break
        exponent += 1