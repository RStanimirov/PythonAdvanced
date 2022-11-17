# RS solution based on lect without functions:
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

    if command == 'up':
        alice_i, alice_j = alice_i - 1, alice_j
        if alice_i < 0 or alice_j < 0 or alice_i >= n or alice_j >= n:
            break
        cell_value = matrix[alice_i][alice_j]
        matrix[alice_i][alice_j] = '*'
        if cell_value == "R":
            break
        if cell_value.isdigit():
            tea_bags += int(cell_value)
            if tea_bags >= 10:
                break

    elif command == 'down':
        alice_i, alice_j = alice_i + 1, alice_j
        if alice_i < 0 or alice_j < 0 or alice_i >= n or alice_j >= n:
            break
        cell_value = matrix[alice_i][alice_j]
        matrix[alice_i][alice_j] = '*'
        if cell_value == "R":
            break
        if cell_value.isdigit():
            tea_bags += int(cell_value)
            if tea_bags >= 10:
                break

    elif command == 'left':
        alice_i, alice_j = alice_i, alice_j - 1
        if alice_i < 0 or alice_j < 0 or alice_i >= n or alice_j >= n:
            break
        cell_value = matrix[alice_i][alice_j]
        matrix[alice_i][alice_j] = '*'
        if cell_value == "R":
            break
        if cell_value.isdigit():
            tea_bags += int(cell_value)
            if tea_bags >= 10:
                break

    elif command == 'right':
        alice_i, alice_j = alice_i, alice_j + 1
        if alice_i < 0 or alice_j < 0 or alice_i >= n or alice_j >= n:
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