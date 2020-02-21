#Just loop through whichever range desired, returns the sum square difference
def sum_dif(numbers):
    sum1 = 0
    sum2 = 0
    for i in range(numbers):
        sum1+=i**2
    for i in range(numbers):
        sum2 += i

    return sum2**2-sum1
