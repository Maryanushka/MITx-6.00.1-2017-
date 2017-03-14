# Problem 3
# 10/10 points (graded)
# Numbers in Mandarin follow 3 simple rules.
#
# There are words for each of the digits from 0 to 10.
# For numbers 11-19, the number is pronounced as "ten digit", so for example, 16 would be pronounced (using Mandarin) as "ten six".
# For numbers between 20 and 99, the number is pronounced as “digit ten digit”, so for example, 37 would be pronounced (using Mandarin) as "three ten seven". If the digit is a zero, it is not included.
# Here is a simple Python dictionary that captures the numbers between 0 and 10.
# Example Usage
#
# convert_to_mandarin('36') will return san shi liu
# convert_to_mandarin('20') will return er shi
# convert_to_mandarin('16') will return shi liu


def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE
    trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
             '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}
    if int(us_num) <= 10:
        for k,v in trans.items():
            if k == str(us_num):
                return v
    if int(us_num) % 10 == 0 and int(us_num) > 10:
        for k, v in trans.items():
            if k == str(us_num)[0]:
                return v + " shi"
    if int(us_num) < 20:
        for k, v in trans.items():
            if k == str(us_num)[1]:
                return "shi " + v
    else:
        for k, v in trans.items():
            if k == str(us_num)[0] and k == str(us_num)[1]:
                first = v
                return first + " shi " + first
            if k == str(us_num)[0]:
                second = v
            elif k == str(us_num)[1]:
                last = v
        return second + " shi " + last

print(convert_to_mandarin(17))