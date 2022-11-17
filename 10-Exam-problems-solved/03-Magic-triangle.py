# def get_magic_triangle(n):
#     triangle = [[1], [1, 1]]
#     for i in range(2, n):
#         current_row = triangle[-1]
#         triangle.append([current_row[0]])
#
#         for j in range(len(current_row) - 1):
#             total = current_row[j] + current_row[j + 1]
#             triangle[i].append(total)
#         triangle[i].append(current_row[-1])
#     return triangle
#
#
# get_magic_triangle(5)

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

n = 5
magic_triangle = [[1], [1, 1]]
for i in range(2, n):
    magic_triangle.append(list('?' * (i + 1)))
    for j in range(i+1):
        if j == 0 or i == j:
            magic_triangle[i][j] = 1
        else:
            magic_triangle[i][j] = magic_triangle[i-1][j-1] + magic_triangle[i-1][j]

for x in magic_triangle:
    print(*x)


