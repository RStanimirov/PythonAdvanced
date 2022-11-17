n = int(input())

bunny = []
matrix = []
for i in range(n):
    elements = input().split()
    matrix.append([])
    for j in range(n):
        if elements[j] == "B":
            bunny = [i, j]
            element = "B"
        elif elements[j] == "X":
            element = "X"
        else:
            element = int(elements[j])
        matrix[i].append(element)


def is_valid(r, c):
    if 0 <= r < n and 0 <= c < n and not matrix[r][c] == "X":
        return True
    return False


def max_points(r, c):
    direction = {"right": 0, "left": 0, "up": 0, "down": 0}
    moves = {"up": [], "down": [], "left": [], "right": []}

    for row in range(r - 1, -1, -1):
        if is_valid(row, c):
            direction["up"] += matrix[row][c]
            moves["up"].append([row, c])
        else:
            break
    for row in range(r + 1, n):
        if is_valid(row, c):
            direction["down"] += matrix[row][c]
            moves["down"].append([row, c])
        else:
            break
    for col in range(c - 1, -1, -1):
        if is_valid(r, col):
            direction["left"] += matrix[r][col]
            moves["left"].append([r, col])
        else:
            break
    for col in range(c + 1, n):
        if is_valid(r, col):
            direction["right"] += matrix[r][col]
            moves["right"].append([r, col])
        else:
            break
    max_points_direction = max(direction, key=lambda x: direction[x])

    print(max_points_direction)
    for move in moves[max_points_direction]:
        print(move)
    print(direction[max_points_direction])


max_points(bunny[0], bunny[1])