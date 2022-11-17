#RS solution modelled on lect solution w/o functions:
n = int(input())

best_intersection = set()

for i in range(n):
    command = input().split('-')
    first_start, first_end = [int(x) for x in command[0].split(',')]
    first_start_end = set(range(first_start, first_end + 1))
    second_star, second_end = [int(x) for x in command[1].split(',')]
    second_start_end = set(range(second_star, second_end + 1))
    current_intersection = first_start_end.intersection(second_start_end)
    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection

#print(f"Longest intersection is [{', '.join([str(x) for x in best_intersection])}] with length {len(best_intersection)}")
# Another, maybe easier to grasp way to print the same is as follows:
print(F"Longest intersection is", end=' ')
print([*best_intersection], sep=', ', end=' ')
print(f"with length {len(best_intersection)}")
