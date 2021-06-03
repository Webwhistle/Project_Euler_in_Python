#!python3
#Finds the largest prime factor to any number
#Let's divide by the smallest prime number, take the result and repeat
#When the loop stops it returns the largest prime factor
def largest_factor(number):
    i = 1
    while i < number:
        i += 1
        if number % i == 0 and number != i:
            number = number/i
    return number

print(largest_factor(2500))
