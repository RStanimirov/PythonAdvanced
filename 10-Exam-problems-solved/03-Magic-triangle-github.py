def get_magic_triangle(n):
    triangle_matrix = [[1], [1, 1]]
    """ The matrix will have n nested lists (or chunks, rows etc.); 
    we already have the first two rows; so we have to generate the next n - 2 rows."""
    for i in range(2, n):
        current_line = []
        for j in range(0, i+1):
            if j == 0:
                current_line.append(1)
            elif j >= len(triangle_matrix[i-1]):
                current_line.append(1)
            else:
                upper_left = triangle_matrix[i - 1][j - 1]
                upper_right = triangle_matrix[i - 1][j]
                summed_value = upper_left + upper_right
                current_line.append(summed_value)

        triangle_matrix.append(current_line)

    return triangle_matrix


print(get_magic_triangle(6))