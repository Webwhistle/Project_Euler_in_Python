import math

"""
We start by picking a number that is divisible by all integers from one to ten. We know that the number we're looking
for has to be divisible by 20, so let's go up in increments of that. With every increment we use modulus to check if
it's divisble by 1 to 20. The first result will be the smallest one and therefore we break there.
"""
i = 2520
divisible_numbers = []
while i < math.factorial(20):
    i += 20
    if i % 20 == i % 19 == i % 18 == i % 17 == i % 16 == i % 15 == i % 14 == i % 13 == i % 12\
    == i % 11 == i % 10 == i % 9 == i % 8 == i % 7 == i % 6 == i % 5 == i % 4\
    == i % 3 == i % 2 == 0:
        divisible_numbers.append(i)
        if i > divisible_numbers[0]:
            break

print(divisible_numbers)
