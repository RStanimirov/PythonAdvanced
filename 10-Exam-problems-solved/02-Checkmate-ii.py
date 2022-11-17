def strike_up(row, col):
    while True:
        next_row, next_col = row - 1, col
        if is_outside(next_row, next_col, n):
            return False
        if matrix[next_row][next_col] == 'K':
            return True
        elif matrix[next_row][next_col] == 'Q':
            return False
        row -= 1


def strike_down(row, col):
    while True:
        next_row, next_col = row + 1, col
        if is_outside(next_row, next_col, n):
            return False
        if matrix[next_row][next_col] == 'K':
            return True
        elif matrix[next_row][next_col] == 'Q':
            return False
        row += 1


def strike_right(row, col):
    while True:
        next_row, next_col = row, col + 1
        if is_outside(next_row, next_col, n):
            return False
        if matrix[next_row][next_col] == 'K':
            return True
        elif matrix[next_row][next_col] == 'Q':
            return False
        col += 1


def strike_left(row, col):
    while True:
        next_row, next_col = row, col - 1
        if is_outside(next_row, next_col, n):
            return False
        if matrix[next_row][next_col] == 'K':
            return True
        elif matrix[next_row][next_col] == 'Q':
            return False
        col -= 1


def strike_up_right_diagonal(row, col):
    while True:
        next_row, next_col = row - 1, col + 1
        if is_outside(next_row, next_col, n):
            return False
        if matrix[next_row][next_col] == 'K':
            return True
        elif matrix[next_row][next_col] == 'Q':
            return False
        row -= 1
        col += 1


def strike_up_left_diagonal(row, col):
    while True:
        next_row, next_col = row - 1, col - 1
        if is_outside(next_row, next_col, n):
            return False
        if matrix[next_row][next_col] == 'K':
            return True
        elif matrix[next_row][next_col] == 'Q':
            return False
        row -= 1
        col -= 1


def strike_down_right_diagonal(row, col):
    while True:
        next_row, next_col = row + 1, col + 1
        if is_outside(next_row, next_col, n):
            return False
        if matrix[next_row][next_col] == 'K':
            return True
        elif matrix[next_row][next_col] == 'Q':
            return False
        row += 1
        col += 1


def strike_down_left_diagonal(row, col):
    while True:
        next_row, next_col = row + 1, col - 1
        if is_outside(next_row, next_col, n):
            return False
        if matrix[next_row][next_col] == 'K':
            return True
        elif matrix[next_row][next_col] == 'Q':
            return False
        row += 1
        col -= 1


def is_outside(row, col, n):
    return row < 0 or col < 0 or row >= n or col >= n


n = 8
matrix = []
queen_i = 0
queen_j = 0
queens_coords = []

for i in range(n):
    line = input().split()
    matrix.append(line)
    for j in range(n):
        element = line[j]
        if element == 'Q':
            queen_i = i
            queen_j = j
            queens_coords.append([queen_i, queen_j])

next_row = 0
next_col = 0
victorious_queens_list = []
for x in queens_coords:
    queen_i, queen_j = x[0], x[1]

    if strike_up(queen_i, queen_j):
        victorious_queens_list.append(x)
    if strike_down(queen_i, queen_j):
        victorious_queens_list.append(x)
    if strike_right(queen_i, queen_j):
        victorious_queens_list.append(x)
    if strike_left(queen_i, queen_j):
        victorious_queens_list.append(x)
    if strike_up_left_diagonal(queen_i, queen_j):
        victorious_queens_list.append(x)
    if strike_up_right_diagonal(queen_i, queen_j):
        victorious_queens_list.append(x)
    if strike_down_left_diagonal(queen_i, queen_j):
        victorious_queens_list.append(x)
    if strike_down_right_diagonal(queen_i, queen_j):
        victorious_queens_list.append(x)

if victorious_queens_list:
    print(*victorious_queens_list, sep='\n')
else:
    print("The king is safe!")