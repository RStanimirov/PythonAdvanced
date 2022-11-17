def is_inside(row, col, length):
    return 0 <= row < length and 0 <= col < length


def check_next_cell(matrix, row, col):
    positions = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)]
    counter = 0
    for x in positions:
        next_row = row + x[0]
        next_col = col + x[1]
        if is_inside(next_row, next_col, len(matrix)):
            next_position = matrix[next_row][next_col]
            if next_position == '*':
                counter += 1
    return counter


n = int(input())
bombs_number = int(input())

matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)

for _ in range(bombs_number):
    # [row, col] = map(lambda x: int(x), input()[1:][:-1].split(', '))
    line_data = input()[1:-1].split(', ')
    row = int(line_data[0])
    col = int(line_data[1])
    # now, place the bombs in the matrix:
    matrix[row][col] = '*'

for row_traverse in range(n):
    for col_traverse in range(n):
        if matrix[row_traverse][col_traverse] != '*':
            counter = check_next_cell(matrix, row_traverse, col_traverse)
            matrix[row_traverse][col_traverse] = counter

for row in matrix:
    print(' '.join([str(x) for x in row]))