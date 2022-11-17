from collections import deque

expression = input().split()

numbers = deque()
result = 0

for x in expression:
    if x in "+-*/":
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            if x == "+":
                result = first_num + second_num
            elif x == "-":
                result = first_num - second_num
            elif x == "*":
                result = first_num * second_num
            elif x == "/":
                result = first_num // second_num

            numbers.appendleft(result)

    else:
        numbers.append(int(x))

print(numbers.popleft())
