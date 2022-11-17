# RS solution 100/100 in judge:
n = int(input())
matrix = []

for _ in range(n):
    line = list(input())
    matrix.append(line)

knights_dict = {}
knights_removed = 0

while True:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'K':
                if 0 <= i - 2 < n and 0 <= j - 1 < n and matrix[i - 2][j - 1] == 'K':
                    knight_position = (i, j)
                    if knight_position not in knights_dict:
                        knights_dict[knight_position] = 0
                    knights_dict[knight_position] += 1
                if 0 <= i - 2 < n and 0 <= j + 1 < n and matrix[i - 2][j + 1] == 'K':
                    knight_position = (i, j)
                    if knight_position not in knights_dict:
                        knights_dict[knight_position] = 0
                    knights_dict[knight_position] += 1
                if 0 <= i + 2 < n and 0 <= j - 1 < n and matrix[i + 2][j - 1] == 'K':
                    knight_position = (i, j)
                    if knight_position not in knights_dict:
                        knights_dict[knight_position] = 0
                    knights_dict[knight_position] += 1
                if 0 <= i + 2 < n and 0 <= j + 1 < n and matrix[i + 2][j + 1] == 'K':
                    knight_position = (i, j)
                    if knight_position not in knights_dict:
                        knights_dict[knight_position] = 0
                    knights_dict[knight_position] += 1
                if 0 <= i - 1 < n and 0 <= j - 2 < n and matrix[i - 1][j - 2] == 'K':
                    knight_position = (i, j)
                    if knight_position not in knights_dict:
                        knights_dict[knight_position] = 0
                    knights_dict[knight_position] += 1
                if 0 <= i - 1 < n and 0 <= j + 2 < n and matrix[i - 1][j + 2] == 'K':
                    knight_position = (i, j)
                    if knight_position not in knights_dict:
                        knights_dict[knight_position] = 0
                    knights_dict[knight_position] += 1
                if 0 <= i + 1 < n and 0 <= j - 2 < n and matrix[i + 1][j - 2] == 'K':
                    knight_position = (i, j)
                    if knight_position not in knights_dict:
                        knights_dict[knight_position] = 0
                    knights_dict[knight_position] += 1
                if 0 <= i + 1 < n and 0 <= j + 2 < n and matrix[i + 1][j + 2] == 'K':
                    knight_position = (i, j)
                    if knight_position not in knights_dict:
                        knights_dict[knight_position] = 0
                    knights_dict[knight_position] += 1

    if knights_dict:
        strongest_knight_position = max(knights_dict, key=lambda x: knights_dict[x])
        i_remove, j_remove = [x for x in strongest_knight_position]
        matrix[i_remove][j_remove] = '0'
        knights_removed += 1
    else:
        break
    knights_dict = {}

print(knights_removed)