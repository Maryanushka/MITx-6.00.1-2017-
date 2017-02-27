

hi = 100
lo = 0
ans = ''
x = (lo + hi)/2
print("Please think of a number between 0 and 100! ")
print("Is your secret number {}?".format(x))
ans = input("Enter 'h' to indicate the guess is too high. "
            "Enter 'l' to indicate the guess is too low. "
            "Enter 'c' to indicate I guessed correctly.")


while  lo < hi and ans != 'c':
    if ans == 'h':
        hi = x
        x = int((lo + x)/2)
        print("Is your secret number {}?".format(x))
        ans=str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    elif ans == 'l':
        lo = x
        x = int((hi + x)/2)
        print("Is your secret number {}?".format(x))
        ans=str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    elif ans == 'c':
        print("Game over. Your secret number was: {}".format(x))
    else:
        while ans not in 'clh':
            print("Sorry, I did not understand your input.")
            print("Is your secret number {}?".format(x))
            ans = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))

print("Game over. Your secret number was: {}".format(x))