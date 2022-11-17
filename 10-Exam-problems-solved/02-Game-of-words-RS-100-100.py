# RS 90/100:
def is_inside(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


string = input()
n = int(input())
matrix = []
player_i, player_j = 0, 0

for i in range(n):
    line = list(input())
    matrix.append(line)
    for j in range(n):
        if matrix[i][j] == 'P':
            player_i, player_j = i, j

num = int(input())

for k in range(num):
    command = input()
    matrix[player_i][player_j] = '-'

    if command == 'up':
        current_i, current_j = player_i - 1, player_j
        if is_inside(current_i, current_j, n):
            if matrix[current_i][current_j] != '-':
                string += matrix[current_i][current_j]
            matrix[current_i][current_j] = 'P'
            player_i, player_j = current_i, current_j
        else:
            matrix[player_i][player_j] = 'P'
            if string:
                string = string[:-1]

    elif command == 'down':
        current_i, current_j = player_i + 1, player_j
        if is_inside(current_i, current_j, n):
            if matrix[current_i][current_j] != '-':
                string += matrix[current_i][current_j]
            matrix[current_i][current_j] = 'P'
            player_i, player_j = current_i, current_j
        else:
            matrix[player_i][player_j] = 'P'
            if string:
                string = string[:-1]

    elif command == 'left':
        current_i, current_j = player_i, player_j - 1
        if is_inside(current_i, current_j, n):
            if matrix[current_i][current_j] != '-':
                string += matrix[current_i][current_j]
            matrix[current_i][current_j] = 'P'
            player_i, player_j = current_i, current_j
        else:
            matrix[player_i][player_j] = 'P'
            if string:
                string = string[:-1]

    elif command == 'right':
        current_i, current_j = player_i, player_j + 1
        if is_inside(current_i, current_j, n):
            if matrix[current_i][current_j] != '-':
                string += matrix[current_i][current_j]
            matrix[current_i][current_j] = 'P'
            player_i, player_j = current_i, current_j
        else:
            matrix[player_i][player_j] = 'P'
            if string:
                string = string[:-1]

print(string)
for x in matrix:
    print(''.join(x))

