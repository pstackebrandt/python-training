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

def calcMultiplesByForLoopWithSteps(multiplier, maxValue, minValue):
    multiples = []
    
    for x in range(minValue, maxValue, multiplier):
            multiples.append(x)

    return multiples


print('Result of:')
print('Multiplication by while loop         : %s' % calcMultiplesByWhileLoop())
resultOfFirstForLoop = calcMultiplesByForLoop(7, 100)
print(f'Multiplication by for loop           : {resultOfFirstForLoop}')
print('Multiplication by for loop with steps: {}'.format(calcMultiplesByForLoopWithSteps(7, 100, 0)))
print('Multiplication by for loop with steps: {}'.format(calcMultiplesByForLoopWithSteps(7, 92, 14)))

print('End of script') 