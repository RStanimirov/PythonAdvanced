import numpy as np

n = 8  # work in progress
chess_board = []
for _ in range(n):
    line = input().split()
    chess_board.append(line)
# . . . . . . . .
# Q . . . . . . .
# . K . . . Q . .
# . . . Q . . . .
# Q . . . Q . . .
# . Q . . . . . .
# . . . . . . Q .
# . Q . Q . . . .
king_i = 0
king_j = 0

matrix = np.array(chess_board)
queen_list = []
horiz_vulnerability = []
vert_vulnerability = []
left_diag_vulnerability = []
right_diag_vilnerability = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'K':
            king_i, king_j = i, j
        if chess_board[i][j] == 'Q':
            queen_i, queen_j = i, j
            queen_list.append([queen_i, queen_j])

for q in queen_list:
    if king_i == q[0]:
        horiz_vulnerability.append([q[0], q[1]])
    elif king_j == q[1]:
        vert_vulnerability.append([q[0], q[1]])

major = np.diagonal(matrix, offset=(king_j - i))
for x in major:
    left_diag_vulnerability.append(x)

minor = np.diagonal(np.rot90(matrix), offset=-matrix.shape[1] + (king_j + i) + 1)
for y in minor:
    right_diag_vilnerability.append(x)

print(horiz_vulnerability)
print(vert_vulnerability)
print(left_diag_vulnerability)
print(right_diag_vilnerability)

