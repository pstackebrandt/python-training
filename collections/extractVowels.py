# extract vowels from a string

WORDS = 'Hello, World!'
ALL_VOWELS = ['a', 'e', 'i', 'o', 'u']

vowels = [x for x in WORDS if x in ALL_VOWELS]

#print('Vowels found: %s in %s' % (vowels, WORDS)) #old style with %s and %
print('Vowels found: {vowels} in {WORDS}')
 
