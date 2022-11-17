matrix = []
for i in range(4):
    matrix.append([])
    for j in range(i*4+1, i*4+4+1):
        matrix[i].append(j)

for x in matrix:
    print(*x, sep=' ')