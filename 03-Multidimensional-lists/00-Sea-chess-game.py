matrix = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

for row_index in range(len(matrix)):
    print(*matrix[row_index])

for _ in range(9):
    row, col = [int(el) for el in input().split(", ")]
    sign = input()
    matrix[row][col] = sign
    for row_index in range(len(matrix)):
        print(*matrix[row_index])