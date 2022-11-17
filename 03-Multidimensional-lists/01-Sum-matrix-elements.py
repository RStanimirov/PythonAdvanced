# rows_columns = [int(x) for x in input().split(', ')]
#
# matrix = []
#
# sum_all_nums = 0
#
# for i in range (rows_columns[0]):
#     matrix.append([int(x) for x in input().split(', ')])
#
# for x in matrix:
#     sum_all_nums += sum(x)
#
# print(sum_all_nums)
# print(matrix)

#RS solution
input_data = input().split(', ')
rows = int(input_data[0])
elements_in_row = int(input_data[1])

matrix = []
sum_matrix = 0

for i in range(rows):
    line = [int(x) for x in input().split(', ')]
    matrix.append(line)
    sum_matrix += sum(line)

print(sum_matrix)
print(matrix)