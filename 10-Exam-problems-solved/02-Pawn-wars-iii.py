def is_inside(size, row, col):
    return 0 <= row < size and 0 <= col < size


size = 8
matrix = []

white_row = 0
white_col = 0
black_row = 0
black_col = 0

cols = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
rows = {0: '8', 1: '7', 2: '6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1'}

for row in range(size):
    line = input().split()
    matrix.append(line)

    for col in range(size):
        if matrix[row][col] == 'w':
            white_col = col
            white_row = row
        elif matrix[row][col] == 'b':
            black_col = col
            black_row = row

is_capture = False
white_steps = 0
black_steps = 0
black_promo = False
white_promo = False

while white_row > 0 and black_row < 7:
    if is_inside(size, white_row - 1, white_col - 1) and matrix[white_row - 1][white_col - 1] == 'b':
        is_capture = True
        white_row = white_row - 1
        white_col = white_col - 1
        white_steps += 1
        break
    elif is_inside(size, white_row - 1, white_col + 1) and matrix[white_row - 1][white_col + 1] == 'b':
        is_capture = True
        white_row = white_row - 1
        white_col = white_col + 1
        white_steps += 1
        break
    elif is_inside(size, white_row + 1, white_col - 1) and matrix[white_row + 1][white_col - 1] == 'b':
        is_capture = True
        white_row = white_row + 1
        white_col = white_col - 1
        white_steps += 1
        break
    elif is_inside(size, white_row + 1, white_col + 1) and matrix[white_row + 1][white_col + 1] == 'b':
        is_capture = True
        white_row = white_row + 1
        white_col = white_col + 1
        white_steps += 1
        break
    else:
        white_row -= 1
        white_steps += 1
        matrix[white_row][white_col] = 'w'
        if white_row == 0:
            white_promo = True
            break
        else:
            if is_inside(size, black_row - 1, black_col - 1) and matrix[black_row - 1][black_col - 1] == 'w':
                is_capture = True
                black_row = black_row - 1
                black_col = black_col - 1
                black_steps += 1
                break
            elif is_inside(size, black_row - 1, black_col + 1) and matrix[black_row - 1][black_col + 1] == 'w':
                is_capture = True
                black_row = black_row - 1
                black_col = black_col + 1
                black_steps += 1
                break
            elif is_inside(size, black_row + 1, black_col - 1) and matrix[black_row + 1][black_col - 1] == 'w':
                is_capture = True
                black_row = black_row + 1
                black_col = black_col - 1
                black_steps += 1
                break
            elif is_inside(size, black_row + 1, black_col + 1) and matrix[black_row + 1][black_col + 1] == 'w':
                is_capture = True
                black_row = black_row + 1
                black_col = black_col + 1
                black_steps += 1
                break
            else:
                black_row += 1
                black_steps += 1
                matrix[black_row][black_col] = 'b'
                if black_row == 7:
                    black_promo = True
                    break
if is_capture:
    if white_steps > black_steps:
        rank = str(cols[white_col]) + str(rows[white_row])
        print(f'Game over! White win, capture on {rank}.')
    else:
        rank = str(cols[black_col]) + str(rows[black_row])
        print(f'Game over! Black win, capture on {rank}.')
else:
    if white_promo:
        rank = str(cols[white_col]) + str(rows[white_row])
        print(f"Game over! White pawn is promoted to a queen at {rank}.")
    else:
        rank = str(cols[black_col]) + str(rows[black_row])
        print(f"Game over! Black pawn is promoted to a queen at {rank}.")