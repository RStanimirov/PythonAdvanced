n = int(input())
matrix = []

for i in range(n):
    matrix.append(input())

searched_element = input()
coordinates = ()

for row in matrix:
    if searched_element in row:
        coordinates = (matrix.index(row), row.j(searched_element))
        print(coordinates)
        break  # break because we need to find the first occurrence of the symbol

if not coordinates:
    print(f"{searched_element} does not occur in the matrix")
