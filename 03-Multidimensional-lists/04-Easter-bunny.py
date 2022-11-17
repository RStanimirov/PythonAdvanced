def move_up(r, c):
    return r-1, c


def move_down(r, c):
    return r+1, c


def move_left(r, c):
    return r, c-1


def move_right(r, c):
    return r, c+1


n = int(input())
matrix = []
bunny_row = 0
bunny_col = 0

# 1) traverse the matrix and find the Bunny's location:
for i in range(n):
    row = input().split()
    matrix.append(row)
    for j in range(n):
        if row[j] == "B":
            bunny_row = i
            bunny_col = j

# 2) initialise a dictionary holding the directional functions - move_up(), move_down(), move_left(), move_right():
directions = {'up': move_up, 'down': move_down, 'left': move_left, 'right': move_right}
best_score = float("-inf")
best_dir = ''
best_path = []

# 3) traverse the dictionary
for key, direction in directions.items():
    current_row, current_col = bunny_row, bunny_col
    current_score = 0
    path = []

    while True:
        current_row, current_col = direction(current_row, current_col)
        if current_row < 0 or current_col < 0 or current_row >= n or current_col >= n:
            break

        if matrix[current_row][current_col] == "X":
            break

        path.append([current_row, current_col])
        current_score += int(matrix[current_row][current_col])

    if current_score > best_score and path:
        best_score = current_score
        best_dir = direction
        best_path = path

print(best_dir)
for x in best_path:
    print(x)
print(best_score)
