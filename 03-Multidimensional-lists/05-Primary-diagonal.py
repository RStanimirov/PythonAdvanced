n = int(input())

matrix = []

for i in range(n):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

diagonal = 0

for i in range(n):
    diagonal += matrix[i][i]

print(diagonal)