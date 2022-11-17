numbers_set_1 = set([int(x) for x in input().split()])
numbers_set_2 = set([int(x) for x in input().split()])
n = int(input())
sub_string = []

for i in range(n):
    command = input().split()

    if command[0] == "Add" and command[1] == "First":
        # [numbers_set_1.add(int(x)) for x in command[2:]]
        for x in command[2:]:
            numbers_set_1.add(int(x))
    elif command[0] == "Add" and command[1] == "Second":
        # [numbers_set_2.add(int(x)) for x in command[2:]]
        for x in command[2:]:
            numbers_set_2.add(int(x))
    elif command[0] == "Remove" and command[1] == "First":
        # numbers_set_1 = numbers_set_1.difference([int(x) for x in command[2:]])su
        for x in command[2:]:
            sub_string.append(int(x))
            numbers_set_1 = numbers_set_1.difference(sub_string)
    elif command[0] == "Remove" and command[1] == "Second":
        # numbers_set_2 = numbers_set_2.difference([int(x) for x in command[2:]])
        for x in command[2:]:
            sub_string.append(int(x))
            numbers_set_2 = numbers_set_2.difference(sub_string)
    else:
        print(numbers_set_1.issubset(numbers_set_2) or numbers_set_2.issubset(numbers_set_1))

print(', '.join(str(x) for x in sorted(numbers_set_1)))
print(', '.join(str(x) for x in sorted(numbers_set_2)))