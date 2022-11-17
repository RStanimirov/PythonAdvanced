n = int(input())
matrix = []
for i in range(n):
    matrix.append(([int(x) for x in input().split()]))

# print(matrix)
command = input()
while command != 'END':
    command_data = command.split()
    if command_data[0] == 'Add':
        row = int(command_data[1])
        column = int(command_data[2])
        value = int(command_data[3])
        if row < 0 or column < 0 or row >= n or column >= n:
            print("Invalid coordinates")
        else:
            matrix[row][column] += value
    if command_data[0] == 'Subtract':
        row = int(command_data[1])
        column = int(command_data[2])
        value = int(command_data[3])
        if row < 0 or column < 0 or row >= n or column >= n:
            print("Invalid coordinates")
        else:
            matrix[row][column] -= value

    command = input()

for x in matrix:
    print(*x)
