e = 1174920
doThis = []
counter = 0
while e != 1:
    if e % 2 == 0:
        e = e / 2
        doThis.append("s")
        counter += 2
    else:
        e = e - 1
        counter += 2
        doThis.append("m")

doThis = doThis[::-1]

g = 13
p = 1300583
current = g
for op in doThis:
    if op == "m":
        current = (current * g) % p
        counter += 2
    if op == "s":
        current = (current * current) % p
        counter += 2
print current
print counter
