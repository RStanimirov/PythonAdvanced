def is_outside_of_matrix(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


entries, sub_entries = [int(x) for x in input().split()]
matrix = []
for _ in range(entries):
    matrix.append(input().split())

command = input()
while command != "END":
    command_data = command.split()

    if len(command_data) == 5 and command_data[0] == 'swap':
        row1, col1, row2, col2 = [int(x) for x in command_data[1:]]
        if is_outside_of_matrix(row1, col1, entries, sub_entries) or \
                is_outside_of_matrix(row2, col2, entries, sub_entries):
            print("Invalid input!")
        else:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

            for x in matrix:
                print(*x)
    else:
        print("Invalid input!")

    command = input()

