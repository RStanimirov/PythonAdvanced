from collections import deque

row, column = [int(x) for x in input().split()]
input_text = list(input())

snake_moves = deque(input_text)
matrix = []
row_sample = []
matrix_grid = row * column

for i in range(1, matrix_grid + 1):
    current_char = snake_moves.popleft()
    snake_moves.append(current_char)
    row_sample.append(current_char)
    if i % column == 0:
        matrix.append(row_sample)
        row_sample = []

for i in range(len(matrix)):
    if i % 2 == 0:
        print(*matrix[i], sep='')
    else:
        print(*matrix[i][::-1], sep='')


