entries, sub_entries = [int(x) for x in input().split(', ')]

matrix = []

for i in range(entries): # 3 cycles
    nums = [int(x) for x in input().split(' ')]
    matrix.append(nums)

# for i in range(sub_entries): # 6 cycles
#     for j in range(entries): # 3 cycles
#         sum_of_columns += matrix[i][j]

for x in range(sub_entries):
    sum_of_columns = []  # sum of the corresponding elements of the nested (sub) entries
    for y in range(entries):
        sum_of_columns.append(matrix[y][x])

    print(sum(sum_of_columns))

