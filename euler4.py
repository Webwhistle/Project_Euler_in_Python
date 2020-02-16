#Beginning attempt at problem 4
def palindrome():
    number = [0,0,0,0,0]
    for i in range(10):
        for j in range(5):
            number[j] = i
    return number
    #return([int(i) for i in str(number)])

print(palindrome())
