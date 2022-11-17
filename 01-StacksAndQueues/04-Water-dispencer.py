# RS (partial) solution:

from collections import deque

water_qty = int(input())
name = input()
queue = deque()

while name != "Start":
    queue.append(name)
    name = input()

command = input()
wanted_liters = 0

while command != "End":
    if command.isdigit():
        wanted_liters = int(command)

        if water_qty >= wanted_liters:
            water_qty -= wanted_liters
            print(f"{queue[0]} got water")
            queue.popleft()
        else:
            print(f"{queue[0]} must wait")
            queue.popleft()
    else:
        refill = command.split()
        water_qty += int(refill[1])

    command = input()

print(f"{water_qty} liters left")
