print('Tree ways to get multiples of 7') 
print('1th - use while loop')

def calcMultiplesByWhileLoop():
    multiples = []
    x = 0
    while x < 100:
        y = x * 7
        x += 1
        if y < 100:
            multiples.append(y)
            
    return multiples

def calcMultiplesByForLoop(multiplier, maxValue):
    multiples = []
    
    for x in range(maxValue):
        y = x * multiplier
        if y < maxValue:
            multiples.append(y)
        else:
            return multiples


print(calcMultiplesByWhileLoop())
print(calcMultiplesByForLoop(7, 100))

print('end') 