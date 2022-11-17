size = 6
matrix = []
score = 0

for row in range(size):
    matrix.append(input().split())

for _ in range(3):
    line = input().split(', ')
    throw_row, throw_col = int(line[0][1]), int(line[1][0])
    if throw_row not in range(size) or throw_col not in range(size):
        continue
    if matrix[throw_row][throw_col] == "B":
        matrix[throw_row][throw_col] = '0'
        for r in range(size):
            score += int(matrix[r][throw_col])

prize = ''

if score < 100:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
elif score < 200:
    prize = 'Football'
elif score < 300:
    prize = 'Teddy Bear'
else:
    prize = 'Lego Construction Set'

if prize:
    print(f"Good job! You scored {score} points, and you've won {prize}.")