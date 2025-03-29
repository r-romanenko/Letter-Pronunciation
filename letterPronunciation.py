# first I need to create a dictionary

letters = {
    'a': 'ay',
    'b': 'bee',
    'c': 'see',
    'd': 'dee',
    'e': 'ee',
    'f': 'eff',
    'g': 'gee',
    'h': 'aitch',
    'i': 'eye',
    'j': 'jay',
    'k': 'kay',
    'l': 'el',
    'm': 'em',
    'n': 'en',
    'o': 'oh',
    'p': 'pee',
    'q': 'cue',
    'r': 'are',
    's': 'ess',
    't': 'tee',
    'u': 'you',
    'v': 'vee',
    'w': 'doubleyou',
    'x': 'ex',
    'y': 'why',
    'z': 'zee'
}

class bcolors:
    BLACK = '\u001b[30m'
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    BLUE = '\u001b[34m'
    MAGENTA = '\u001b[35m'
    CYAN = '\u001b[36m'
    WHITE = '\u001b[37m'
    RESET = '\u001b[0m'

# go through the letters in the dictionary.
# for each letter, make a new string and add it to a list (later)
# get the pronunciation, and then go through that pronunciation one more time

pronunciations = []

for key in letters.keys():
    curWord = key
    journey = f"{curWord}"
    
    for i in range(3):
        # go through all letters
        newWord = ""
        for letter in curWord:
            newWord += letters[letter]

        # go through the newWord, seeing how much the curWord overlaps
        journey += f", {bcolors.GREEN}"

        letter_added = False

        index = len(curWord)
        for j in range(len(curWord)):
            if curWord[j] != newWord[i]:
                # if i == 0:
                #     journey += newWord[0]
                index = j + 1
                break
            else:
                journey += newWord[j]
                letter_added = True
        
        journey += bcolors.RESET
        if not letter_added:
            journey += newWord[0]
        # index += 1

        while index < len(newWord):
            journey += newWord[index]
            index += 1
        

        curWord = newWord
        # journey += f", {curWord}"
    pronunciations.append(journey)
    
for journ in pronunciations:
    print(journ)




print()