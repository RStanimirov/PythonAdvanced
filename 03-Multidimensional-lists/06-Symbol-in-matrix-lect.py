n = int(input())

matrix = []

for _ in range(n):
    matrix.append(input())

searched_char = input()
position = None

for i in range(n):
    for j in range(n):
        current_char = matrix[i][j]
        if searched_char == current_char:
            position = (i, j)
            print(position)
            break
    if position:
        break

if not position:
    print(f"{searched_char} does not occur in the matrix")
