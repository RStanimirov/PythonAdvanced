n = int(input())
number_stack = []
curr_max = 0
curr_min = 0

for i in range(n):
    command = [int(x) for x in input().split()]
    if command[0] == 1:
        parameter = int(command[1])
        number_stack.append(parameter)
    elif command[0] == 2 and number_stack:
        number_stack.pop()
    elif command[0] == 3 and number_stack:
        curr_max = max(number_stack)
        print(curr_max)
    elif command[0] == 4 and number_stack:
        curr_min = min(number_stack)
        print(curr_min)

while number_stack:
    element = number_stack.pop()
    if number_stack:
        print(element, end=', ')
    else:
        print(element)

