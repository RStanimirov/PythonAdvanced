entries, sub_entries = [int(x) for x in input().split()]

matrix = []

for _ in range(entries):
    matrix.append([int(x) for x in input().split()])

max_sum = - 9999999999999999
max_sum_matrix = []

for i in range(entries - 2):
    for j in range(sub_entries - 2):
        current_sub_matrix = [matrix[i][j], matrix[i][j+1], matrix[i][j+2],\
                              matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2],\
                              matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]]
        current_sum = sum(current_sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_matrix = current_sub_matrix.copy()

print(f"Sum = {max_sum}")
print(max_sum_matrix[0], max_sum_matrix[1], max_sum_matrix[2])
print(max_sum_matrix[3], max_sum_matrix[4], max_sum_matrix[5])
print(max_sum_matrix[6], max_sum_matrix[7], max_sum_matrix[8])








