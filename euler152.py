#!python3

#invq = inverse squares
def invq(n):
    return (n**2)**-1

sum = 0
for i in range(2,80):
    sum += invq(i)

print(sum)
