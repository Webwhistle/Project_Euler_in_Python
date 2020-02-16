import numpy as np

#Find the sum of all even terms in the fibonacci sequence up to four million
#We start by initiating a list with zeros using numpy

#Create a fibonacci function with starting elements and length as parameters
def fibonacci(n1,n2,length):
    fib_list = np.zeros(length)
    fib_list[0],fib_list[1] = n1,n2
    for i in range(2,length,1):
        fib_list[i] = int(fib_list[i-1] + fib_list[i-2])
        fib_list = [int(i) for i in fib_list]
    return fib_list[length-1], fib_list

#Find the fibonacci sequence where the last element is smaller than four million
i = 1
while True:
    i+= 1
    number, fib_list = fibonacci(1,2,i)
    fibonacci(1,2,i)
    if number > 4*10**6:
        break

#Loop over all elements and sum the evens
sum = 0
for i in fib_list:
    if i % 2 == 0:
        sum = sum + i

print(sum)
