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

    # the current Queen attempts to strike up:
    queen_i, queen_j = x[0], x[1]
    while True:
        next_row, next_col = queen_i-1, queen_j
        if is_outside(next_row, next_col, n):
            break
        if matrix[next_row][next_col] == 'K':
            victorious_queens_list.append(x)
        elif matrix[next_row][next_col] == 'Q':
            break
        queen_i -= 1

    # the current Queen attempts to strike down:
    queen_i, queen_j = x[0], x[1]
    while True:
        next_row, next_col = queen_i+1, queen_j
        if is_outside(next_row, next_col, n):
            break
        if matrix[next_row][next_col] == 'K':
            victorious_queens_list.append(x)
        elif matrix[next_row][next_col] == 'Q':
            break
        queen_i += 1

    # the current Queen attempts to strike left:
    queen_i, queen_j = x[0], x[1]
    while True:
        next_row, next_col = queen_i, queen_j-1
        if is_outside(next_row, next_col, n):
            break
        if matrix[next_row][next_col] == 'K':
            victorious_queens_list.append(x)
        elif matrix[next_row][next_col] == 'Q':
            break
        queen_j -= 1

    # the current Queen attempts to strike right:
    queen_i, queen_j = x[0], x[1]
    while True:
        next_row, next_col = queen_i, queen_j+1
        if is_outside(next_row, next_col, n):
            break
        if matrix[next_row][next_col] == 'K':
            victorious_queens_list.append(x)
        elif matrix[next_row][next_col] == 'Q':
            break
        queen_j += 1

    # the current Queen attempts to strike up left diagonal:
    queen_i, queen_j = x[0], x[1]
    while True:
        next_row, next_col = queen_i-1, queen_j-1
        if is_outside(next_row, next_col, n):
            break
        if matrix[next_row][next_col] == 'K':
            victorious_queens_list.append(x)
        elif matrix[next_row][next_col] == 'Q':
            break
        queen_i -= 1
        queen_j -= 1

    # the current Queen attempts to strike up right diagonal:
    queen_i, queen_j = x[0], x[1]
    while True:
        next_row, next_col = queen_i-1, queen_j+1
        if is_outside(next_row, next_col, n):
            break
        if matrix[next_row][next_col] == 'K':
            victorious_queens_list.append(x)
        elif matrix[next_row][next_col] == 'Q':
            break
        queen_i -= 1
        queen_j += 1

    # the current Queen attempts to strike down left diagonal:
    queen_i, queen_j = x[0], x[1]
    while True:
        next_row, next_col = queen_i+1, queen_j-1
        if is_outside(next_row, next_col, n):
            break
        if matrix[next_row][next_col] == 'K':
            victorious_queens_list.append(x)
        elif matrix[next_row][next_col] == 'Q':
            break
        queen_i += 1
        queen_j -= 1

    # the current Queen attempts to strike down right diagonal:
    queen_i, queen_j = x[0], x[1]
    while True:
        next_row, next_col = queen_i+1, queen_j+1
        if is_outside(next_row, next_col, n):
            break
        if matrix[next_row][next_col] == 'K':
            victorious_queens_list.append(x)
        elif matrix[next_row][next_col] == 'Q':
            break
        queen_i += 1
        queen_j += 1

if victorious_queens_list:
    print(*victorious_queens_list, sep='\n')
else:
    print("The king is safe!")