def is_outside(r, c, n):
    if r < 0 or c < 0 or r >= n or c >= n:
        return True
    else:
        return False


def get_next_position(command, r, c):
    if command == "up":
        return r - 1, c
    if command == "down":
        return r + 1, c
    if command == "left":
        return r, c - 1
    if command == "right":
        return r, c + 1


n = int(input())
matrix = []

alice_i, alice_j = 0, 0

for i in range(n):
    line = input().split()
    matrix.append(line)
    for j in range(n):
        cell = line[j]
        if cell == 'A':
            alice_i, alice_j = i, j


tea_bags = 0
matrix[alice_i][alice_j] = '*'

while True:
    command = input()
    alice_i, alice_j = get_next_position(command, alice_i, alice_j)
    if is_outside(alice_i, alice_j, n):
        break

    cell_value = matrix[alice_i][alice_j]
    matrix[alice_i][alice_j] = '*'
    if cell_value == "R":
        break

    if cell_value.isdigit():
        tea_bags += int(cell_value)
        if tea_bags >= 10:
            break

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for x in matrix:
    print(' '.join(x))
