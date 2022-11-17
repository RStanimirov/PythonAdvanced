matrix_entries = int(input())

matrix = []
flattened_matrix = []

# for i in range(rows):
#     nums = [int(x) for x in input().split(', ')]
#     matrix.extend(nums)

for entry in range(matrix_entries):
    sub_entries = [int(x) for x in input().split(', ')]
    matrix.append(sub_entries)

for entry in range(len(matrix)):
    for sub_entry in range(len(matrix[entry])):
        flattened_matrix.append(matrix[entry][sub_entry])

print(flattened_matrix)
