# w6 p.130 Kofler:Python-2024

# Create a dictionary german - english

words = {
    'eins': 'one',
    'zwei': 'two',
    'drei': 'three',
    'vier': 'four',
    'fünf': 'five',
    'sechs': 'six',
    'sieben': 'seven',
    'acht': 'eight',
    'neun': 'nine'
}

print('Get words by key')
print(f'eins is {words['eins']}')
print(f'acht is {words['acht']}')

print('Get all keys and values by items() in a loop')
for key, value in words.items():
    print(f'{key} is {value}')