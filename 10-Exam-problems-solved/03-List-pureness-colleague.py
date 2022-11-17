from collections import deque


def best_list_pureness(*args):
    best_pureness = float('-inf')
    sum_of_pureness = 0
    deq = deque(args[0])
    count = args[1]
    rotations = 0
    if count <= 0:
        count = 1
    for rotation in range(count):
        for index in range(len(deq)):
            sum_of_pureness += (deq[index] * index)

        if sum_of_pureness > best_pureness:
            best_pureness = sum_of_pureness
            rotations = rotation
        num = deq.pop()
        deq.appendleft(num)
        sum_of_pureness = 0

    return f"Best pureness {best_pureness} after {rotations} rotations"


# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
