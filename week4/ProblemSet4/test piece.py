# SCRABBLE_LETTER_VALUES = {
#     'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
# }
#
# def getWordScore(word, n):
#     """
#     Returns the score for a word. Assumes the word is a valid word.
#
#     The score for a word is the sum of the points for letters in the
#     word, multiplied by the length of the word, PLUS 50 points if all n
#     letters are used on the first turn.
#
#     Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
#     worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
#
#     word: string (lowercase letters)
#     n: integer (HAND_SIZE; i.e., hand size required for additional points)
#     returns: int >= 0
#     """
#     SCRABBLE_LETTER_VALUES = {
#             'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
#             'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
#         }
#
#     def wordScore(word):
#         """
#
#         :param word: is string
#         :return: scrore of letters in the string
#         """
#         summary = 0
#         for i in word:
#             if i in SCRABBLE_LETTER_VALUES:
#                 summary +=SCRABBLE_LETTER_VALUES[i]
#         return summary*len(word)
#
#     if len(word) == n:
#         return wordScore(word)+50
#     else:
#         return wordScore(word)
#
# print(getWordScore('was', 7))



# def updateHand(hand, word):
#     """
#     Assumes that 'hand' has all the letters in word.
#     In other words, this assumes that however many times
#     a letter appears in 'word', 'hand' has at least as
#     many of that letter in it.
#
#     Updates the hand: uses up the letters in the given word
#     and returns the new hand, without those letters in it.
#
#     Has no side effects: does not modify hand.
#
#     word: string
#     hand: dictionary (string -> int)
#     returns: dictionary (string -> int)
#     """
#     temp = hand
#     for i in word:
#         if i in temp:
#             if temp[i]!=0:
#                 temp[i] -= 1
#             else:
#                 temp[i] = temp[i]
#     return temp
# print(updateHand({'i': 1, 'p': 0, 'o': 1, 'a': 1, 'l': 1, 'e': 0, 'y': 1}, 'apple'))

# , wordList
def isValidWord(word, hand):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    inFile = open("words.txt", 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())

    temp = hand.copy()
    g = {}
    if word in wordList:
        for i in word:
            if i in temp:
                g = i
                if temp[i] > 0:
                    temp[i] -= 1
                else:
                    return False
            else:
                return False
    else:
        return False
    if g in word:
        return True
print(isValidWord('rapture', {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}))


def playHand(hand, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """

    inFile = open("words.txt", 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score

    # As long as there are still letters left in the hand:
    while n > 0:
        # Display the hand
        print('Current Hand: '+hand)
        # Ask user for input
        word = str(input('Enter word, or a "." to indicate that you are finished: '))
        # If the input is a single period:
        if word == '.':
            return


        # End the game (break out of the loop)


        # Otherwise (the input is not a single period):

        # If the word is not valid:

        # Reject invalid word (print a message followed by a blank line)

        # Otherwise (the word is valid):

        # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line

        # Update the hand


        # Game is over (user entered a '.' or ran out of letters), so tell user the total score


print(playHand({'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}, ))