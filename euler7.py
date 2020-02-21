"""
We use the function in the extras folder that lists all primes up to a given length.
We also use the fact that the number of primes y is roughly equal x/log(x) where x is a number
larger but close to the largest prime in y. Therefore if y is 10 001, then x is around 120 000.
The function is rather slow (95sec) and needs to be improved.
"""

def sieve(length):
    numbers = range(2,length) #Primes start at 2
    for n in range(2,length): #Loop for divisors
        for i in numbers:     #Loop for each number in list
            if i % n == 0 and i != n:
                numbers.remove(i)
    return numbers

primes = sieve(120000)
print(primes[10000])
