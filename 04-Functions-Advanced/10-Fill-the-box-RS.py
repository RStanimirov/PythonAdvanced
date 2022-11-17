# RS solution 60/100 in Judge:
def fill_the_box(height, length, width, *args):
    box_volume = height * length * width
    box_filled = 0
    all_cubes = [x for x in args if x != 'Finish']
    cubes_capacity = sum(all_cubes)
    remaining_space = 0
    remaining_cubes = 0

    for x in args:
        if x != 'Finish':
            if x > (box_volume - box_filled):
                remainder = x - (box_volume - box_filled)
                box_filled += x - remainder
                remaining_cubes = cubes_capacity - box_filled
                remaining_space = box_volume - box_filled
                if box_filled == box_volume:
                    break
            else:
                box_filled += x
                remaining_cubes = cubes_capacity - box_filled
                remaining_space = box_volume - box_filled
                if box_filled == box_volume:
                    break
        else:
            break

    if remaining_space > 0:
        return f"There is free space in the box. You could put {remaining_space} more cubes."
    else:
        return f"No more free space! You have {remaining_cubes} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
