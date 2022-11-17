def print_upper_part(n):
    for upper_row in range(1, n+1):
        for j in range(1, upper_row+1):
            print(j, end=' ')
        print()


def print_lower_part(n):
    for lower_row in range(n-1, 0, -1):
        for j in range(1, lower_row+1):
            print(j, end=' ')
        print()


def print_numbers_triangle(n):
    print_upper_part(n)
    print_lower_part(n)

