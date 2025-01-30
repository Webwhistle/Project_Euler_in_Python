import sys, os

#Open the txt file as a matrix
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname('euler11.txt')))

with open(os.path.join(__location__, 'euler11.txt')) as f:
    data = [[int(cell.strip()) for cell in row.rstrip(' ').split(' ')] for row in f]

tdata = [list(i) for i in zip(*data)]
edata = enumerate(data)

def hv_product(data):
    largest_sum = []
    for row in data:
        sum_list = []
        for i in range(15):
            sum_list.append(row[i]*row[i+1]*row[i+2]*row[i+3])
        largest_sum.append(max(sum_list))
    return max(largest_sum)

for row, count in zip(edata, range(1,6)):
    sum_list = []
    for i in range(15):
        sum_list.append(row[1][i] * edata[count][i+1] * edata[count+1][i+2])

def up_horizontal_sums():
    largest_sum = []
    for i in range(17):
        sum_list = []
        for j in range(17):
            sum_list.append(data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3])
        largest_sum.append(max(sum_list))
    return max(largest_sum)

def down_horizontal_sums():
    largest_sum = []
    for i in range(17):
        sum_list = []
        for j in range(17):
            sum_list.append(data[19-i][19-j]*data[19-i-1][19-j-1]*data[19-i-2][19-j-2]*data[19-i-3][19-j-3])
        largest_sum.append(max(sum_list))
    return max(largest_sum)

