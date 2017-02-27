# def isWordGuessed(secretWord, lettersGuessed):
#     '''
#     secretWord: string, the word the user is guessing
#     lettersGuessed: list, what letters have been guessed so far
#     returns: boolean, True if all the letters of secretWord are in lettersGuessed;
#       False otherwise
#     '''
#     # FILL IN YOUR CODE HERE...
#     word = ''
#     for i in range(len(secretWord)):
#         if secretWord[i] in lettersGuessed:
#             word += secretWord[i]
#     if word == secretWord:
#         return True
#     else:
#         return False


#
#
# def getGuessedWord(secretWord, lettersGuessed):
#     '''
#     secretWord: string, the word the user is guessing
#     lettersGuessed: list, what letters have been guessed so far
#     returns: string, comprised of letters and underscores that represents
#       what letters in secretWord have been guessed so far.
#     '''
#     # FILL IN YOUR CODE HERE...
#     word = ''
#
#     for i in range(len(secretWord)):
#         if secretWord[i] in lettersGuessed:
#             word += secretWord[i]
#         else:
#             word += '_ '
#     return word


# def getAvailableLetters(lettersGuessed):
#     '''
#     lettersGuessed: list, what letters have been guessed so far
#     returns: string, comprised of letters that represents what letters have not
#       yet been guessed.
#     '''
#     # FILL IN YOUR CODE HERE...
#     test= ['a','b','c','d','e','f','g','h','i','j','k',
#        'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     for i in range(len(lettersGuessed)):
#         if lettersGuessed[i] in test:
#             test.remove(lettersGuessed[i])
#     return ''.join(test)





