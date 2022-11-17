def is_inside(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


n = int(input())
matrix = []
lair_list = []
snake_i, snake_j = 0, 0

for i in range(n):
    line = list(input())
    matrix.append(line)
    for j in range(n):
        if matrix[i][j] == 'S':
            snake_i, snake_j = i, j
        if matrix[i][j] == 'B':
            burrow_i, burrow_j = i, j
            lair_list.append([i, j])

food_counter = 0
is_outside = False

while True:
    command = input()
    matrix[snake_i][snake_j] = '.'

    if command == 'up':
        next_i, next_j = snake_i - 1, snake_j
        if is_inside(next_i, next_j, n):
            if matrix[next_i][next_j] == 'B':
                matrix[next_i][next_j] = '.'
                next_i, next_j = lair_list[1][0], lair_list[1][1]
            elif matrix[next_i][next_j] == '*':
                matrix[next_i][next_j] = '.'
                food_counter += 1
            matrix[next_i][next_j] = 'S'
            snake_i, snake_j = next_i, next_j
            if food_counter >= 10:
                break
        else:
            is_outside = True
            break

    elif command == 'down':
        next_i, next_j = snake_i + 1, snake_j
        if is_inside(next_i, next_j, n):
            if matrix[next_i][next_j] == 'B':
                matrix[next_i][next_j] = '.'
                next_i, next_j = lair_list[1][0], lair_list[1][1]
            elif matrix[next_i][next_j] == '*':
                matrix[next_i][next_j] = '.'
                food_counter += 1
            matrix[next_i][next_j] = 'S'
            snake_i, snake_j = next_i, next_j
            if food_counter >= 10:
                break
        else:
            is_outside = True
            break

    elif command == 'left':
        next_i, next_j = snake_i, snake_j - 1
        if is_inside(next_i, next_j, n):
            if matrix[next_i][next_j] == 'B':
                matrix[next_i][next_j] = '.'
                next_i, next_j = lair_list[1][0], lair_list[1][1]
            elif matrix[next_i][next_j] == '*':
                matrix[next_i][next_j] = '.'
                food_counter += 1
            matrix[next_i][next_j] = 'S'
            snake_i, snake_j = next_i, next_j
            if food_counter >= 10:
                break
        else:
            is_outside = True
            break

    elif command == 'right':
        next_i, next_j = snake_i, snake_j + 1
        if is_inside(next_i, next_j, n):
            if matrix[next_i][next_j] == 'B':
                matrix[next_i][next_j] = '.'
                next_i, next_j = lair_list[1][0], lair_list[1][1]
            elif matrix[next_i][next_j] == '*':
                matrix[next_i][next_j] = '.'
                food_counter += 1
            matrix[next_i][next_j] = 'S'
            snake_i, snake_j = next_i, next_j
            if food_counter >= 10:
                break
        else:
            is_outside = True
            break

if is_outside:
    print("Game over!")
    print(f"Food eaten: {food_counter}")

if food_counter >= 10:
    print("You won! You fed the snake.")
    print(f"Food eaten: {food_counter}")

for x in matrix:
    print(''.join(x))
