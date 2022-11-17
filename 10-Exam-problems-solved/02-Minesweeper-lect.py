def is_inside(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def define_cells_value(r, c, field):
    counter = 0
    if is_inside(r-1, c, len(matrix)) and matrix[r-1][c] == '*':
        counter += 1
    if is_inside(r+1, c, len(matrix)) and matrix[r+1][c] == '*':
        counter += 1
    if is_inside(r, c-1, len(matrix)) and matrix[r][c-1] == '*':
        counter += 1
    if is_inside(r, c+1, len(matrix)) and matrix[r][c+1] == '*':
        counter += 1
    if is_inside(r-1, c-1, len(matrix)) and matrix[r-1][c-1] == '*':
        counter += 1
    if is_inside(r+1, c-1, len(matrix)) and matrix[r+1][c-1] == '*':
        counter += 1
    if is_inside(r-1, c+1, len(matrix)) and matrix[r-1][c+1] == '*':
        counter += 1
    if is_inside(r+1, c+1, len(matrix)) and matrix[r+1][c+1] == '*':
        counter += 1
    return counter


n = int(input())

# 1) first of all, we make an empty matrix (containing only zeroes):
matrix = []
for _ in range(n):
    matrix.append([0]*n)

bombs_count = int(input())

# 2) traverse the field to place the bombs:
for _ in range(bombs_count):
    bomb_data = input()[1:-1].split(', ')
    row = int(bomb_data[0])
    col = int(bomb_data[1])
    matrix[row][col] = '*'

# 3) now, lets traverse the field to give value to the empty cells:
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '*': # if we find a bomb, we continue to the next cell:
            continue
        cell_value = define_cells_value(i, j, matrix)
        matrix[i][j] = cell_value

# 4) finally, print the matrix:
for x in matrix:
    print(*x)