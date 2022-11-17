def possible_hits(row, col, board, n):
    knight = board[row][col]
    hits = 0
    if 0 <= row-2 < n and 0 <= col-1 < n and board[row - 2][col - 1] == knight:
        hits += 1
    if 0 <= row-2 < n and 0 <= col+1 < n and board[row - 2][col + 1] == knight:
        hits += 1
    if 0 <= row+2 < n and 0 <= col-1 < n and board[row + 2][col - 1] == knight:
        hits += 1
    if 0 <= row+2 < n and 0 <= col+1 < n and board[row + 2][col + 1] == knight:
        hits += 1
    if 0 <= row-1 < n and 0 <= col-2 < n and board[row - 1][col - 2] == knight:
        hits += 1
    if 0 <= row-1 < n and 0 <= col+2 < n and board[row - 1][col + 2] == knight:
        hits += 1
    if 0 <= row+1 < n and 0 <= col-2 < n and board[row + 1][col - 2] == knight:
        hits += 1
    if 0 <= row+1 < n and 0 <= col+2 < n and board[row + 1][col + 2] == knight:
        hits += 1
    return hits


# RS solution based on C# solution in forum:
""" For each "K" there are max 8 positions that can "hit", i.e. 8 positions that need to be checked 
and the result compared with the others to eliminate the "K" with the maximum result. 
The loop till 0 hits solves the problem with the minimum number; maybe another solution is 
to filter in descending order. """

n = int(input())
matrix = []
for _ in range(n):
    line = list(input())
    matrix.append(line)

max_hits = 1
max_row = 0
max_col = 0
counter = 0

while max_hits > 0:
    max_hits = 0
    for i in range(n):
        for j in range(n):
            search_coord = matrix[i][j]
            if search_coord == "K":
                hits = possible_hits(i, j, matrix, n)
                if hits > max_hits:
                    max_hits = hits
                    max_row = i
                    max_col = j
    if max_hits > 0:
        matrix[max_row][max_col] = '0'
        counter += 1

print(counter)


