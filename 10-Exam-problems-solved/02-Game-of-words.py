def next_position(direction, row, col):
    if direction == 'down':
        return row + 1, col
    elif direction == 'up':
        return row -1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1


string = input()
n = int(input())
matrix = []
player_i = 0
player_j = 0

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'P':
            player_j = row
            player_i = col

num = int(input())

for _ in range(num):
    command = input()

    new_row, new_col = next_position(command, player_j, player_i)
    if new_row < 0 or new_col < 0 or new_row >= n or new_col >= n:
        if string:
            string = string[:-1]
        continue
    matrix[player_j][player_i] = '-'
    player_j, player_i = new_row, new_col

    if matrix[player_j][player_i] != '-':
        string += matrix[player_j][player_i]

    matrix[player_j][player_i] = 'P'

print(string)

for i in range(n):
    print(*matrix[i], sep='')