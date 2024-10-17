# Task: Extract vowels from a string
# Script contains different versions 

WORDS = 'Hello, World!'
ALL_VOWELS = ['a', 'e', 'i', 'o', 'u']
ALL_VOWELS_STR = ''.join(ALL_VOWELS)

def extractVowelsByListComprehension(words, allVowels):
    return [x for x in words if x in allVowels]

vowelsFromCompre = extractVowelsByListComprehension(WORDS, ALL_VOWELS)
print(f'Vowels found by list comprehension: {vowelsFromCompre} in {WORDS}')

#print('Vowels found by list comprehension: %s in %s' % (vowelsFromCompre, WORDS)) #old style with %s and %


def extractVowelsByFilterWithFunc(words, allVowelsStr):
    def filterVowels(char):
        if char in allVowelsStr:
            return True
    
    return list(filter(filterVowels, words))

vowelsFromFilter = extractVowelsByFilterWithFunc(WORDS, ALL_VOWELS_STR)
print(f'Vowels found by filter with function: {vowelsFromFilter} in {WORDS}')


def extractVowelsByFilterWithLambda(words, allVowelsStr):
    return list(filter(lambda char: char in allVowelsStr, words))

vowelsFromFilter = extractVowelsByFilterWithLambda(WORDS, ALL_VOWELS_STR)
print(f'Vowels found by filter with lambda: {vowelsFromFilter} in {WORDS}')
