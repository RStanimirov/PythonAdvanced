# RS modelled on another solution:
n = 6
matrix = []

for i in range(n):
    line = input().split()
    matrix.append(line)

total_points = 0
prize = ''

for attempt in range(3):
    command = [int(x) for x in input().strip('()').split(', ')]
    throw_i, throw_j = command[0], command[1]

    if throw_i < 0 or throw_j < 0 or throw_i >= n or throw_j >= n:
        continue

    if matrix[throw_i][throw_j] == 'B':
        for i in range(n):
            if matrix[i][throw_j].isdigit():
                total_points += int(matrix[i][throw_j])
        # You can hit a bucket only once. If you hit the same bucket again, you do not score any points:
        matrix[throw_i][throw_j] = 'X'

        if 100 <= total_points <= 199:
            prize = 'Football'
        elif 200 <= total_points <= 299:
            prize = 'Teddy Bear'
        elif total_points >= 300:
            prize = 'Lego Construction Set'

if prize == "Football":
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif prize == "Teddy Bear":
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
elif prize == "Lego Construction Set":
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
else:
    print(f'Sorry! You need {100 - total_points} points more to win a prize.')