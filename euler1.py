#Find the sum of all multiples of 3 and 5 below 1000
#We do this by creating a list with all multiples
#Iterate over the list and sum each element to a local variable
def sum(num):
    suml = []
    sum = 0
    for i in range(num):
        if i*3 < num:
            suml.append(i*3)
        if i*5 < num:
            suml.append(i*5)
    for i in set(suml):
        sum += i
    print(sum)

sum(1000)
