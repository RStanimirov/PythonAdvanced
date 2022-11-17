def fill_the_box(height, length, width, *args):
    volume = height * length * width
    cubes_left = 0

    for x in args:
        if x == 'Finish':
            break

        if x > volume:
            x -= volume
            cubes_left += x
            volume = 0
        else:
            volume -= x

    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {cubes_left} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))