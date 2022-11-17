def gen_seq(range_by_input):
    start, end = [int(x) for x in range_by_input.split(',')]
    return set(range(start, end + 1))


n = int(input())

best_intersection = set()

for i in range(n):
    command = input().split('-')
    first_part = gen_seq(command[0])
    second_part = gen_seq(command[1])
    current_intersection = first_part.intersection(second_part)
    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection

print(f"Longest intersection is [{', '.join([str(x) for x in best_intersection])}] with length {len(best_intersection)}")

# Another, maybe easier to grasp way to print the same is as follows:
# print(F"Longest intersection is", end=' ')
# print([*best_intersection], sep=', ', end=' ')
# print(f"with length {len(best_intersection)}")












