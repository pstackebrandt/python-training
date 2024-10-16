print('Three ways to get multiples of 7')



def calcMultiplesByWhileLoop(multiplier, maxValue, minValue):
    multiples = []
    x = minValue
    while x < maxValue:
        y = x * multiplier
        x += 1
        if y < maxValue:
            multiples.append(y)
        else:
            break
            
    return multiples

# max verbose solution
def calcMultiplesByForLoop(multiplier, maxValue, minValue):
    multiples = []
    
    for x in range(minValue, maxValue):
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

# best solution    
def calcMultiplesByComprehension(multiplier, maxValue, minValue):
    return [x * 7 for x in range(minValue, maxValue//multiplier + 1)]

print('Result of:')
print('Multiplication by while loop         : %s' % calcMultiplesByWhileLoop(7, 100, 0))
resultOfFirstForLoop = calcMultiplesByForLoop(7, 100, 0)
print(f'Multiplication by for loop           : {resultOfFirstForLoop}')
print('Multiplication by for loop with steps: {}'.format(calcMultiplesByForLoopWithSteps(7, 100, 0)))
print('Multiplication by list comprension:    {}'.format(calcMultiplesByComprehension(7, 100, 0)))

print('\nDifferent values:')
print('Multiplication by for loop with steps: {}'.format(calcMultiplesByForLoopWithSteps(7, 92, 14)))

print('End of script') 