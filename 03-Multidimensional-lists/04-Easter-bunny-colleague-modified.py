def is_valid(r, c):
    if 0 <= r < n and 0 <= c < n and not matrix[r][c] == "X":
        return True
    return False


n = int(input())
bunny_coord = []
matrix = []

for i in range(n):
    elements = input().split()
    matrix.append([])
    for j in range(n):
        if elements[j] == "B":
            bunny_coord = [i, j]
            element = "B"
        elif elements[j] == "X":
            element = "X"
        else:
            element = int(elements[j])
        matrix[i].append(element)

direction_dict = {"right": 0, "left": 0, "up": 0, "down": 0}
path_dict = {"up": [], "down": [], "left": [], "right": []}
current_r, current_c = bunny_coord[0], bunny_coord[1]

for row in range(current_r - 1, -1, -1):
    if is_valid(row, current_c):
        direction_dict["up"] += matrix[row][current_c]
        path_dict["up"].append([row, current_c])
    else:
        break
for row in range(current_r + 1, n):
    if is_valid(row, current_c):
        direction_dict["down"] += matrix[row][current_c]
        path_dict["down"].append([row, current_c])
    else:
        break
for col in range(current_c - 1, -1, -1):
    if is_valid(current_r, col):
        direction_dict["left"] += matrix[current_r][col]
        path_dict["left"].append([current_r, col])
    else:
        break
for col in range(current_c + 1, n):
    if is_valid(current_r, col):
        direction_dict["right"] += matrix[current_r][col]
        path_dict["right"].append([current_r, col])
    else:
        break
max_points = max(direction_dict, key=lambda x: direction_dict[x])

print(max_points)
for x in path_dict[max_points]:
    print(x)
print(direction_dict[max_points])


