# RS solution after the exam, for the exam submitted a 100/100 solution based on a colleagues solution in C#:
chess_matrix = [['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
                ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
                ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
                ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
                ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
                ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
                ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
                ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]

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

    if (0 <= white_i - 1 < n and 0 <= white_j - 1 < n) and matrix[white_i - 1][white_j - 1] == 'b':
        print(f"Game over! White win, capture on {chess_matrix[white_i - 1][white_j - 1]}.")
        break

    elif (0 <= white_i - 1 < n and 0 <= white_j + 1 < n) and matrix[white_i - 1][white_j + 1] == 'b':
        print(f"Game over! White win, capture on {chess_matrix[white_i - 1][white_j + 1]}.")
        break

    else:
        matrix[white_i][white_j] = '-'
        white_i -= 1
        matrix[white_i][white_j] = 'w'

        if white_i == 0:
            print(f"Game over! White pawn is promoted to a queen at {chess_matrix[white_i][white_j]}.")
            break

    if (0 <= black_i + 1 < n and 0 <= black_j - 1 < n) and matrix[black_i + 1][black_j - 1] == 'w':
        print(f"Game over! Black win, capture on {chess_matrix[black_i + 1][black_j - 1]}.")
        break

    elif (0 <= black_i + 1 < n and 0 <= black_j + 1 < n) and matrix[black_i + 1][black_j + 1] == 'w':
        print(f"Game over! Black win, capture on {chess_matrix[black_i + 1][black_j + 1]}.")
        break

    else:
        matrix[black_i][black_j] = '-'
        black_i += 1
        matrix[black_i][black_j] = 'b'

        if black_i == 7:
            print(f"Game over! Black pawn is promoted to a queen at {chess_matrix[black_i][black_j]}.")
            break
