def get_next_position(direction, r, c):
    if direction == 'up':
        return r-1, c
    elif direction == 'down':
        return r+1, c
    elif direction == 'left':
        return r, c-1
    elif direction == 'right':
        return r, c+1


presents = int(input())
n = int(input())

matrix = []
santa_row = 0
santa_column = 0
total_good_kids = 0
good_kids_with_presents = 0

# First we locate the position of Santa in the natrix and we count all good kids:
for i in range(n):
    line = input().split()
    matrix.append(line)
    for j in range(n):
        if line[j] == 'V':
            total_good_kids += 1
        elif line[j] == 'S':
            santa_row = i
            santa_column = j

command = input()

# Then we get the new position of Santa defined by the input commands.
# We have made the get_next_position function beforehand:
while command != 'Christmas morning':
    # but before moving to the text position, we should clear the old position:
    matrix[santa_row][santa_column] = '-'
    santa_row, santa_column = get_next_position(command, santa_row, santa_column)

    if matrix[santa_row][santa_column] == 'V':
        presents -= 1
        good_kids_with_presents += 1
        matrix[santa_row][santa_column] = 'S'

    elif matrix[santa_row][santa_column] == 'X':
        matrix[santa_row][santa_column] = 'S'

    elif matrix[santa_row][santa_column] == 'C':
        matrix[santa_row][santa_column] = 'S'
        if matrix[santa_row][santa_column - 1] == 'V' and presents:
            presents -= 1
            good_kids_with_presents += 1
            matrix[santa_row][santa_column -1 ] = '-'
        elif matrix[santa_row][santa_column - 1] == 'X' and presents:
            presents -= 1
            matrix[santa_row][santa_column - 1] = '-'
        if matrix[santa_row][santa_column + 1] == 'V' and presents:
            presents -= 1
            good_kids_with_presents += 1
            matrix[santa_row][santa_column + 1] = '-'
        elif matrix[santa_row][santa_column + 1] == 'X' and presents:
            presents -= 1
            matrix[santa_row][santa_column + 1] = '-'
        if matrix[santa_row - 1][santa_column] == 'V' and presents:
            presents -= 1
            good_kids_with_presents += 1
            matrix[santa_row - 1][santa_column] = '-'
        elif matrix[santa_row - 1][santa_column] == 'X' and presents:
            presents -= 1
            matrix[santa_row - 1][santa_column] = '-'
        if matrix[santa_row + 1][santa_column] == 'V' and presents:
            presents -= 1
            good_kids_with_presents += 1
            matrix[santa_row + 1][santa_column] = '-'
        elif matrix[santa_row + 1][santa_column] == 'X' and presents:
            presents -= 1
            matrix[santa_row + 1][santa_column] = '-'
    # We break only if Santa is out of presents or if all the good kids have received their present:
    if presents == 0 or good_kids_with_presents == total_good_kids:
        break

    command = input()

if presents == 0 and good_kids_with_presents < total_good_kids:
    print("Santa ran out of presents!")

for x in matrix:
    print(' '.join(x))

if good_kids_with_presents == total_good_kids:
    print(f"Good job, Santa! {good_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {total_good_kids - good_kids_with_presents} nice kid/s.")
