# Create a dictionary of chests with fruits.
# Start with 2 collections that contain chests and fruits.
# Join them and create the dictionary.
# Show the content of first, last and 3rd chest - numbers from original chest list.
# Show all fruits in chests by for loop.

print('I create a dictionary of chests from lists')

chests = ['orangesChest', 'appleChest', 'cherryChest']
fruits = ['oranges', 'apples', 'cherries', 'cucumbers'] # Additional list entry will be ignored.

chestsAndFruits = zip(chests, fruits)
fruitChests = dict(chestsAndFruits)

print(f'\nMy fruits in chests: %s' % fruitChests)
print(f'first chest: %s' % fruitChests[chests[0]])
print(f'third chest: %s' % fruitChests[chests[2]])
print(f'last chest: %s' % fruitChests[chests[-1]])

print(f"\nI'm proud to own this fruits:")
for chest, fruit in fruitChests.items():
    if chest == chests[-1]:
        print('lovely ' + str(fruit))
    else:
        print(fruit)