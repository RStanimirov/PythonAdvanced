# RS solution:
from collections import deque


def best_list_pureness(*args):
    numbers = deque(args[0])
    n = args[1]
    rotations_dict = {}
    best_sum = - 999999999

    for i in range(n+1):
        current_sum = 0
        for j in range(len(numbers)):
            current_sum += numbers[j] * j
        if current_sum > best_sum:
            best_sum = current_sum
        if current_sum not in rotations_dict:
            rotations_dict[current_sum] = i
        numbers.rotate()

    best_pureness = max(rotations_dict.keys())
    best_rotation = rotations_dict[best_pureness]
    return f"Best pureness {best_pureness} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
