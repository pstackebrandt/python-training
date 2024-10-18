# w7 p.130 Kofler:Python-2024

# Get length of the longest word of a sentence.
# =============================================

# A first simple and verbose version with custom maxWord function.

# expects string and returns string
def removeSpecialCharacters(sentence):
    alfaNumSpaceOnly = filter(lambda x: x.isalnum() or x.isspace(), sentence)
    return ''.join(alfaNumSpaceOnly)

# expects list with single words
def getMaxWordLength(words):
    maxLength = 0
    for word in words:
        currLenght = len(word)
        # check whether current word is longer than longest found so far
        # if longer -> save currentLength as maxLength
        maxLength = max(currLenght, maxLength)
    return maxLength

SENTENCE = 'Lorem ipsum dolor sit amet, sed diam voluptua. At vero'
wordsStr = removeSpecialCharacters(SENTENCE)
words =  wordsStr.split()
maxLength = getMaxWordLength(words)

print(words)
print(f'Longest word has {maxLength} characters.')    
