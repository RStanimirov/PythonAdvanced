n = int(input())
matrix = []
even_nums = []

for i in range(n):
    # even_nums = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    # matrix.append(even_nums)
    line = [int(x) for x in input().split(', ')]
    line_with_evens = []
    for x in line:
        if x % 2 == 0:
            line_with_evens.append(x)
    matrix.append(line_with_evens)
print(matrix)
