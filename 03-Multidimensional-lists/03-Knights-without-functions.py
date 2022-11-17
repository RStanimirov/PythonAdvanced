n = int(input())
matrix = []
for _ in range(n):
    line = list(input())
    matrix.append(line)

knights_on_board = []

for i in range(n):
    for j in range(n):
        search_coord = matrix[i][j]
        if search_coord == "K":
            knights_on_board.append([i, j])

knights_to_be_removed = 0

while True:
    arh = []
    for k_r, k_c in knights_on_board:
        possible_hits = [
            [k_r - 2, k_c - 1], [k_r - 2, k_c + 1],
            [k_r - 1, k_c - 2], [k_r - 1, k_c + 2],
            [k_r + 2, k_c + 1], [k_r + 1, k_c + 2],
            [k_r + 2, k_c - 1], [k_r + 1, k_c - 2]
        ]
        count = 0
        for hit_r, hit_c in possible_hits:
            if hit_r in range(n) and hit_c in range(n):
                if matrix[hit_r][hit_c] == "K":
                    count += 1

        arh.append([count, k_r, k_c])

    chek = [el[0] for el in arh]
    if len(chek) == chek.count(0):
        break
    arh_sor = sorted(arh, key=lambda x: -x[0])
    matrix[arh_sor[0][1]][arh_sor[0][2]] = 0
    knights_on_board.remove([arh_sor[0][1], arh_sor[0][2]])
    knights_to_be_removed += 1

print(knights_to_be_removed)