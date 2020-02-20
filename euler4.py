#Generate all six-digit palindromes
def palindrome():
    palindromes = []
    number = [0,0,0,0,0,0]
    for i in range(9,-1,-1):
        number[0], number[-1] = i, i
        for j in range(9,-1,-1):
            number[1], number[-2] = j, j
            for k in range(9,-1,-1):
                number[2], number[-3] = k,k
                palindromes.append(int(''.join(str(v) for v in number)))
    palindromes = [ele for ele in palindromes if ele > 99999]
    return palindromes

#Find all three-digit factors to all six-digit palindromes
def factors():
    factors = []
    palindromes = palindrome()
    for i in palindromes:
        for j in range(999,99,-1):
            if i%j == 0 and i/j < 1000:
                print([i,j,i/j])

factors()
