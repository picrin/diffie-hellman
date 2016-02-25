bigUgly = 1300583
checkNumber = 13
currentNumber = checkNumber
checked = 1
counter = 0
while currentNumber != 12:
    currentNumber = (currentNumber * checkNumber) % bigUgly
    counter += 2
    checked += 1
print checked
print counter
