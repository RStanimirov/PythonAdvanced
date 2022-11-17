n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))


def look_around(k, matrix):
    power = 0
    # Right down:
    if 0 <= (k[1] + 2) < n and 0 <= (k[0] + 1) < n:
        right_d = (k[0] + 1, k[1] + 2)
        if matrix[right_d[0]][right_d[1]] == 'K':
            power += 1
    # Right up:
    if 0 <= (k[1] + 2) < n and 0 <= (k[0] - 1) < n:
        right_u = (k[0] - 1, k[1] + 2)
        if matrix[right_u[0]][right_u[1]] == 'K':
            power += 1
    # Left down:
    if 0 <= (k[1] - 2) < n and 0 <= (k[0] + 1) < n:
        left_d = (k[0] + 1, k[1] - 2)
        if matrix[left_d[0]][left_d[1]] == 'K':
            power += 1
    # Left up:
    if 0 <= (k[1] - 2) < n and 0 <= (k[0] - 1) < n:
        left_u = (k[0] - 1, k[1] - 2)
        if matrix[left_u[0]][left_u[1]] == 'K':
            power += 1
    # Up left:
    if 0 <= (k[0] - 2) < n and 0 <= (k[1] - 1) < n:
        up_l = (k[0] - 2, k[1] - 1)
        if matrix[up_l[0]][up_l[1]] == 'K':
            power += 1
    # Up right:
    if 0 <= (k[0] - 2) < n and 0 <= (k[1] + 1) < n:
        up_r = (k[0] - 2, k[1] + 1)
        if matrix[up_r[0]][up_r[1]] == 'K':
            power += 1
    # Down left:
    if 0 <= (k[0] + 2) < n and 0 <= (k[1] - 1) < n:
        down_l = (k[0] + 2, k[1] - 1)
        if matrix[down_l[0]][down_l[1]] == 'K':
            power += 1
    # Down right:
    if 0 <= (k[0] + 2) < n and 0 <= (k[1] + 1) < n:
        down_r = (k[0] + 2, k[1] + 1)
        if matrix[down_r[0]][down_r[1]] == 'K':
            power += 1
    return power

# 1) function to find the strongest knight, i.e. reaching the greatest number of other knights:
def get_knights():
    strongest = (0, 0, 0)
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 'K':
                klock = (r, c)
                power = look_around(klock, matrix)
                if power > 0 and power > strongest[2]:
                    strongest = (r, c, power)
    return strongest


knights = get_knights()
count = 0

while not knights[2] == 0:
    r, c = knights[0], knights[1]
    # 2) remove the strongest knight by replacing 'K' with '0':
    matrix[r][c] = '0'
    # 3) check again for strongest knight (or a knight which reaches at least 1 other knight). If not, the program quits.
    knights = get_knights()
    count += 1

print(count)