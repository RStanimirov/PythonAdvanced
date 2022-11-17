def is_valid(r, rows):
    return r > 0 and r <= rows


matrix = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

rows_input = int(input())

if is_valid(rows_input, len(matrix)):
    print("Valid input! I made a-one-row function which checks if the input is a valid row in a matrix!")
else:
    print("Invalid input!")






