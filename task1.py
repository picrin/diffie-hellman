p = 1300583
g = 13

currentNumber = g
counter = 1
while currentNumber != 12:
    currentNumber = (currentNumber * g) % p
    counter += 1
print counter
