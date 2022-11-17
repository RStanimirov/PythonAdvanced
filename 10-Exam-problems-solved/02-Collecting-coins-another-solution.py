#  100/100
from math import floor

size = int(input())
matrix = []
player_coords = []
total_coins = 0
player_path = []
game_over = False

for row in range(size):
    line = input().split()
    matrix.append(line)
    for idx in range(len(line)):
        if line[idx] == "P":
            player_coords = [row, idx]
            player_path = [[row, idx]]


def turn(player, direction):
    if direction == "up":
        player[0] -= 1
    elif direction == "down":
        player[0] += 1
    elif direction == "right":
        player[1] += 1
    elif direction == "left":
        player[1] -= 1

    if player[0] < 0:
        player[0] += size
    elif player[0] > size - 1:
        player[0] -= size
    elif player[1] < 0:
        player[1] += size
    elif player[1] > size - 1:
        player[1] -= size

    return player


def game(field, player, coins):
    game_over = False
    row = player[0]
    col = player[1]
    if field[row][col] == "X":
        coins = floor(coins / 2)
        game_over = True
        return game_over, coins, field
    elif field[row][col] == "P":
        coins += 0
        field[row][col] = 0
    else:
        coins += int(field[row][col])
        field[row][col] = 0
    return game_over, coins, field


while True:
    cmd = input()
    result = turn(player_coords, cmd).copy()
    player_path.append(result)
    game_over, total_coins, matrix = game(matrix, result, total_coins)
    if game_over or total_coins >= 100:
        break

if total_coins >= 100:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")
print(f"Your path:")
print(*player_path, sep="\n")