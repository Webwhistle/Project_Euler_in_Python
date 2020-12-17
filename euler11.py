import sys, os

#Open the txt file as a matrix
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname('euler11.txt')))

with open(os.path.join(__location__, 'euler11.txt')) as f:
    data = [[int(cell.strip()) for cell in row.rstrip(' ').split(' ')] for row in f]

def horizontal_sums(data):
    largest_sum = []
    for row in data:
        sum_list = []
        for i in range(6):
            sum_list.append(row[i]*row[i+1]*row[i+2]*row[i+3])
        largest_sum.append(max(sum_list))
    return max(largest_sum)

def vertical_sums(data):
    largest_sum = []
    for i in range(9):
        sum_list = []
        for j in range(6):
            sum_list.append(data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3])
        largest_sum.append(max(sum_list))
    return max(largest_sum)

def horizontal_sums(data):
    pass
