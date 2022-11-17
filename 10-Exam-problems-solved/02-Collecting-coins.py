# def is_inside(row, col, size):
#     return 0 <= row < size and 0 <= col < size
#
#
# def get_next_position(direction, r, c):
#     if direction == "up":
#         return r - 1, c
#     if direction == "down":
#         return r + 1, c
#     if direction == "left":
#         return r, c - 1
#     if direction == "right":
#         return r, c + 1

def calculate_position(ma, r, c):
    pass

n = int(input())

matrix = []

for row in range(n):
    line = input().split()
    matrix.append(line)
    for column in range(n):
        current_position = line[column]
        if current_position == 'P':
            player_row, player_column = row, column
            player_position = matrix[row, column]

coins_collected = 0
player_path = []
player_path.append(player_position)

while True:
    # player_row, player_column = get_next_position(command, player_row, player_column)
    command = input()
    # if command == 'up' and is_inside():
    #     pass
    # elif command == 'down' and is_inside():
    #     pass
    # elif command == 'left' and is_inside():
    #     pass
    # elif command == 'right' and is_inside():
    #     pass


