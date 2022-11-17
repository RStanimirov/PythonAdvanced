# RS solution:
from collections import deque

males_stack = [int(x) for x in input().split()]
females_que = deque([int(x) for x in input().split()])
counter = 0

while males_stack and females_que:
    current_male = males_stack[-1]
    current_female = females_que[0]

    if current_male <= 0 or current_female <= 0:
        if current_male <= 0:
            males_stack.pop()
        elif current_female <= 0:
            females_que.popleft()

    elif current_male % 25 == 0 or current_female % 25 == 0:
        if current_male % 25 == 0:
            males_stack.pop()
            if males_stack:
                males_stack.pop()
        if current_female % 25 == 0:
            females_que.popleft()
            if females_que:
                females_que.popleft()

    elif current_male != current_female:
        if females_que:
            females_que.popleft()
        if males_stack:
            males_stack[-1] -= 2

    else:
        counter += 1
        males_stack.pop()
        females_que.popleft()

print(f"Matches: {counter}")
if males_stack:
    print(f"Males left: {', '.join(str(x) for x in reversed(males_stack))}")
else:
    print("Males left: none")
if females_que:
    print(f"Females left: {', '.join(str(x) for x in females_que)}")
else:
    print("Females left: none")