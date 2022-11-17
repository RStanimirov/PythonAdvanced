def set_position(row, col):
    result = ''
    counter = 8
    for i in range(8):
        if col == i:
            result += chr(i+97)
    for j in range(8):
        if row == j:
            result += str(counter)
        counter -= 1
    return result


def is_inside(row, col):
    if 0 <= row <= 7 and 0 <= col <= 7:
        return True
    return False


n = 8
matrix = []

white_i, white_j = 0, 0
black_i, black_j = 0, 0

for _ in range(n):
    line = input().split()
    matrix.append(line)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'w':
            white_i, white_j = i, j
        if matrix[i][j] == 'b':
            black_i, black_j = i, j

while True:

    if is_inside(white_i - 1, white_j - 1) and matrix[white_i - 1][white_j - 1] == 'b':
        print(f"Game over! White win, capture on {set_position(white_i - 1, white_j - 1)}.")
        break

    elif is_inside(white_i - 1, white_j + 1) and matrix[white_i - 1][white_j + 1] == 'b':
        print(f"Game over! White win, capture on {set_position(white_i - 1, white_j + 1)}.")
        break

    else:
        matrix[white_i][white_j] = '-'
        white_i -= 1
        matrix[white_i][white_j] = 'w'

        if white_i == 0:
            print(f"Game over! White pawn is promoted to a queen at {set_position(white_i, white_j)}.")
            break

    if is_inside(black_i + 1, black_j - 1) and matrix[black_i + 1][black_j - 1] == 'w':
        print(f"Game over! Black win, capture on {set_position(black_i + 1, black_j - 1)}.")
        break

    elif is_inside(black_i + 1, black_j + 1) and matrix[black_i + 1][black_j + 1] == 'w':
        print(f"Game over! Black win, capture on {set_position(black_i + 1, black_j + 1)}.")
        break

    else:
        matrix[black_i][black_j] = '-'
        black_i += 1
        matrix[black_i][black_j] = 'b'

        if black_i == 7:
            print(f"Game over! Black pawn is promoted to a queen at {set_position(black_i, black_j)}.")
            break
