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

print(calcMultiplesByWhileLoop())

print('end') 