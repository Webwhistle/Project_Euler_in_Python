#!python3
import itertools, secrets
from math import sqrt

def miller_rabin(w, iterations = 50):
    """ Primality test of a number w. It's a probability function with an error
        of pow(2,-100). Given 50 iterations it is assumed the risk of false
        primes is less than pow(2,-100) if the prime is less than 2048 bits.
        """
    a = 0
    m = w-1
    while m % 2 == 0:
        a += 1 # largest int: pow(2,a) divides w-1
        m //= 2
    for _ in range(1,iterations):
        b = secrets.randbelow(w-1)
        if b <= 1:
            continue
        z = pow(b, m, w)
        if z == 1 or z == w - 1:
            continue
        for _ in range(a-1):
            z = pow(z, 2, w)
            if z == w - 1:
                break
        else:
            return "COMPOSITE"
    return "PROBABLY PRIME"

def largest_pandigital(n):
    number_list = reversed([str(i+1) for i in range(n)])
    permutations = list(itertools.permutations(number_list))
    return permutations

def create_int(n):
    number_list = []
    for numbers in largest_pandigital(n):
        n_number = int("".join(numbers))
        number_list.append(n_number)
    return number_list

n_list = create_int()
primes = []
for i in n_list:
    if miller_rabin(i) == "PROBABLY PRIME":
        primes.append(i)

print(len(n_list))
print(max(primes))
