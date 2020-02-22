import math

"""
By defining a,b,c as a sum that will equal 1000 and then looping until it
satisfies the pythagorean triplet we get the numbers we're looking for.
"""
a = 0
b = 0
c = 1000 - a - b
triplet = []
for i in range(1000):
    a = i
    for n in range(1000):
        b = n
        if 1000 - a - b == math.sqrt(a**2+b**2) and a < b < c and a != 0:
            c = 1000 - a - b
            triplet.append(a)
            triplet.append(b)
            triplet.append(c)

print(triplet[0]*triplet[1]*triplet[2])
