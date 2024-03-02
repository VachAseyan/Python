import random

# 1
def generate_random_matrix(rows, cols):
    matrix = []
    for x in range(rows):
        row = []
        for x in range(cols):
            random_number = random.randint(1, 100)
            row.append(random_number)
        matrix.append(row)
    return matrix

rows = 3
cols = 4
random_matrix = generate_random_matrix(rows, cols)
for row in random_matrix:
    print(row)

# 2

def get_column_sum(matrix, indexColumn):
    column_sum = 0
    for column in matrix:
        column_sum += column[indexColumn]
    return column_sum

matrix = [
    [21, 2, 35, 4],
    [5, 51, 60, 54],
    [75, 8, 9, 61]
]

indexColumn = 3
column_sum = get_column_sum(matrix,indexColumn)
print("Սյունակը", indexColumn,indexColumn,"րդ սյունակի գումարը", column_sum)

#3

def get_row_average(matrix, rowIndex):
    row = matrix[rowIndex]
    row_sum = sum(row)
    row_average = row_sum / len(row)
    return row_average

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rowIndex = 2
row_average = get_row_average(matrix, rowIndex)
print("Նշված",rowIndex, "տողի միջինը", row_average)