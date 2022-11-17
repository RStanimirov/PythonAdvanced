from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
operators = deque(input().split())

total_honey = 0

while bees and nectar:
    current_bee = bees[0]
    current_nectar = nectar[-1]
    current_operator = operators[0]
    if current_nectar >= current_bee:
        if current_operator == '+':
            current_honey = abs(current_bee + current_nectar)
            operators.popleft()
            bees.popleft()
            nectar.pop()
            total_honey += current_honey
        elif current_operator == '-':
            current_honey = abs(current_bee - current_nectar)
            operators.popleft()
            bees.popleft()
            nectar.pop()
            total_honey += current_honey
        elif current_operator == '*':
            current_honey = current_bee * current_nectar
            operators.popleft()
            bees.popleft()
            nectar.pop()
            total_honey += current_honey
        elif current_operator == '/':
            if current_nectar == 0:
                current_honey = 0
                operators.popleft()
                bees.popleft()
                nectar.pop()
                total_honey += current_honey
            else:
                current_honey = current_bee / current_nectar
                operators.popleft()
                bees.popleft()
                nectar.pop()
                total_honey += current_honey

    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
