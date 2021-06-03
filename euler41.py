import itertools, math

def n_pandigital(n):
    number_list = [str(i) for i in range(n)]
    permutations = list(itertools.permutations(number_list))
    n_permutations = []
    for numbers in permutations:
        if numbers[0] != "0":
            n_number = "".join(numbers)
            n_permutations.append(int(n_number))
    return (n_permutations)

print(n_pandigital(10))
