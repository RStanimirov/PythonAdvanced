# a colleague's solution with "lazy" traversing (with nested loops) through the matrix, as he put it.
def is_valid(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True


def calc_cell(r, c, ma):
    bombs = 0
    for r_move in range(-1, 2):
        for c_move in range(-1, 2):
            r_check = r + r_move
            c_check = c + c_move
            if is_valid(r_check, c_check) and ma[r_check][c_check] == "*":
                bombs += 1
    return bombs


n = int(input())
bombs_num = int(input())

matrix = [[0] * n for _ in range(n)]

for _ in range(bombs_num):
    row, col = eval(input())
    matrix[row][col] = "*"

for i in range(n):
    for j in range(n):
        if not matrix[i][j] == "*":
            matrix[i][j] = calc_cell(i, j, matrix)

for row in matrix:
    print(*row)