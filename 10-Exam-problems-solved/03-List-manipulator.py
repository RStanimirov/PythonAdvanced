from collections import deque


def list_manipulator(*args):
    numbers = deque(args[0])
    first_command = args[1]
    second_command = args[2]
    if first_command == 'add' and second_command == 'beginning':
        if len(args) > 3:
            third_command = args[3:]
            for i in range(len(third_command)-1, -1, -1):
                numbers.appendleft(third_command[i])
        else:
            third_command = args[3]
            numbers.appendleft(third_command)

    elif first_command == 'add' and second_command == 'end':
        if len(args) > 3:
            third_command = args[3:]
            for i in range(len(third_command)):
                numbers.append(third_command[i])
        else:
            third_command = args[3]
            numbers.append(third_command)
    elif first_command == 'remove' and second_command == 'beginning':
        if len(args) > 3:
            third_command = args[3]
            for i in range(third_command):
                numbers.popleft()
        else:
            numbers.popleft()
    elif first_command == 'remove' and second_command == 'end':
        if len(args) > 3:
            third_command = args[3]
            for i in range(third_command):
                numbers.pop()
        else:
            numbers.pop()
    return list(numbers)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
