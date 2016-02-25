exponentiation = 1174920
toDo = []

p = 1300583
g = 13

countOps = 0

while exponentiation != 1:
    if exponentiation % 2 == 0:
        exponentiation /= 2
        toDo.append("s")
        countOps += 2
    else:
        exponentiation -= 1
        countOps += 1
        toDo.append("m")

toDo = toDo[::-1]
currentNumber = g
for operation in toDo:
    if operation == "s":
        currentNumber = (currentNumber * currentNumber) % p
        countOps += 3
    if operation == "m":
        currentNumber = (currentNumber * g) % p
        countOps += 3
print currentNumber
print countOps
