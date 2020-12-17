#!python3

def sqrt(x):
    return x**0.5

def sieve(length):
    """ Creates a list with all the primes up to a chosen length. """
    numbers = {i:True for i in range(2,length)} # Primes start at 2
    for i in range(2, int(sqrt(length))+1):     # Loop for divisors
        if numbers[i]:
            for j in range(i**2,length,i):      # Loop for each number in list
                numbers[j] = False
    return [i for i in numbers if numbers[i]]

prime_list = sieve(2*10**6)
sum = 0
for i in prime_list:
    sum+=i

print(sum)
