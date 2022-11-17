# RS modelled on lect, added is_inside() function:
def is_inside(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


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
bunny_i = 0
bunny_j = 0

# 1) traverse the matrix and find the Bunny's location:
for i in range(n):
    line = input().split()
    matrix.append(line)
    # check the location of the bunny
    for j in range(n):
        if line[j] == "B":
            bunny_i = i
            bunny_j = j

# 2) initialise a dictionary holding the directional functions - move_up(), move_down(), move_left(), move_right():
directions = {'up': move_up, 'down': move_down, 'left': move_left, 'right': move_right}

# 3) initialise the wanted outputs of the task:
best_direction = ''
best_path = []
best_score = float("-inf")

# 4) traverse the dictionary
for key, function in directions.items():
    current_row, current_col = bunny_i, bunny_j
    current_score = 0
    bunny_path = []

    while True:
        current_row, current_col = function(current_row, current_col)
        if not is_inside(current_row, current_col, n):
            break
        if matrix[current_row][current_col] == "X":
            break

        bunny_path.append([current_row, current_col])
        current_score += int(matrix[current_row][current_col])

    if current_score > best_score and bunny_path:
        best_score = current_score
        best_direction = key
        best_path = bunny_path

print(best_direction)
for x in best_path:
    print(x)
print(best_score)
