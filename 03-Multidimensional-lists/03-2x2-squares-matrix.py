rows, elements_in_row = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

# sub_matrices_list = []
# for i in range(rows - 1):
#     for j in range(elements_in_row - 1):
#         sub_matrices_list.append(matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1])
# print(sub_matrices_list) # ['ABEB', 'BBBB', 'BDBB', 'EBIJ', 'BBJB', 'BBBB']

counter = 0

for i in range(rows - 1):
    for j in range(elements_in_row - 1):
        # total 6 loops
        current_sub_matrix = [matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]]
        # print(current_sub_matrix)
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            counter += 1

print(counter)
