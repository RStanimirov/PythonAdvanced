# The task is to generate a numbered chessboard, like below:
chess_matrix = [['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
                ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
                ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
                ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
                ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
                ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
                ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
                ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]

# one solution would be as follows:
n = 8
matrix = []

for i in range(n):
    line = [f"{'a'+str(n-i)}", f"{'b'+str(n-i)}", f"{'c'+str(n-i)}", f"{'d'+str(n-i)}", f"{'e'+str(n-i)}", f"{'f'+str(n-i)}", f"{'g'+str(n-i)}", f"{'h'+str(n-i)}"]
    matrix.append(line)


# below is another optimised solution:
coor_board = []

for row in range(8):
    coor_board.append([f'' for el in range(8)])
    for col in range(8):
        coor_board[row][col] = f'{chr(97 + col)}{8 - row}'

for x in coor_board:
    print(x)
