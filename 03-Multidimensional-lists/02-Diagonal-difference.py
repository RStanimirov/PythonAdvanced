n = int(input())

matrix = []

for i in range(n):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

primary_diagonal_list = []
primary_diagonal_sum = 0
secondary_diagonal_list = []
secondary_diagonal_sum = 0

for i in range(n):
    primary_diagonal_list.append(matrix[i][i])
    primary_diagonal_sum += matrix[i][i]
for j in range(n):
    secondary_diagonal_list.append(matrix[j][n-1-j])
    secondary_diagonal_sum += matrix[j][n-1-j]

print(abs(primary_diagonal_sum - secondary_diagonal_sum))

