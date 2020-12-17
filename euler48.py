def powersums(number, digits):
    sum = 0
    for i in range(1,number):
        sum += i**i
    return (str(sum)[digits:])

print(powersums(1000,-10))
