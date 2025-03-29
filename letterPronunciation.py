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
        curWord = newWord
        journey += f", {curWord}"
    pronunciations.append(journey)
    
for journ in pronunciations:
    print(journ)