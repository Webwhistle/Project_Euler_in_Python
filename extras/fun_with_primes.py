#Create a list with all the primes up to a chosen length
def sieve(length):
    numbers = [range(2,length)] #Primes start at 2
    for n in range(2,length): #Loop for divisors
        for i in numbers:     #Loop for each number in list
            if i % n == 0 and i != n:
                numbers.remove(i)
    return numbers

#Create a list with all prime factors to a number
def pfactors(number):
    primes = sieve(number)
    factors = []
    for i in primes:
        if number % i == 0:
            factors.append(i)
    return factors

print(len(sieve(100000)))
