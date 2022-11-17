n = 8
matrix = []
queens_list = []
king_i, king_j = None, None
for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == 'K':
            king_i, king_j = i, j
            break
step = 0
while True:  # checking same row - right
    if matrix[king_i][king_j + step] == 'Q':
        queens_list.append([king_i, king_j + step])
        break
    step += 1
    if king_j + step >= n:
        break
step = 0
while True:  # checking same row - left
    if matrix[king_i][king_j + step] == 'Q':
        queens_list.append([king_i, king_j + step])
        break
    step -= 1
    if king_j + step < 0:
        break
step = 0
while True:  # checking same col, down
    if matrix[king_i + step][king_j] == 'Q':
        queens_list.append([king_i + step, king_j])
        break
    step += 1
    if king_i + step >= n:
        break
step = 0
while True:  # checking same col, up
    if matrix[king_i + step][king_j] == 'Q':
        queens_list.append([king_i + step, king_j])
        break
    step -= 1
    if king_i + step < 0:
        break
step = 0
while True:  # checking diagonal up-left
    if matrix[king_i + step][king_j + step] == 'Q':
        queens_list.append([king_i + step, king_j + step])
        break
    step -= 1
    if king_j + step < 0 or king_i + step < 0:
        break

step = 0
while True:  # checking diagonal up-right
    if matrix[king_i + step][king_j - step] == 'Q':
        queens_list.append([king_i + step, king_j - step])
        break
    step -= 1
    if king_j - step >= n or king_i + step < 0:
        break

step = 0
while True:  # checking diagonal down-right
    if matrix[king_i + step][king_j + step] == 'Q':
        queens_list.append([king_i + step, king_j + step])
        break
    step += 1
    if king_j + step >= n or king_i + step >= n:
        break

step = 0
while True:  # checking diagonal down-left
    if matrix[king_i + step][king_j - step] == 'Q':
        queens_list.append([king_i + step, king_j - step])
        break
    step += 1
    if king_j - step < 0 or king_i + step >= n:
        break

if queens_list:
    print(*queens_list, sep='\n')
else:
    print("The king is safe!")
