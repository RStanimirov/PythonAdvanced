from collections import deque

number_of_pumps = int(input())
pumps_route = deque()

for i in range(number_of_pumps):
    pump_data = [int(x) for x in input().split()]
    pumps_route.append(pump_data)

for attempt in range(number_of_pumps):
    tank = 0

    for x in pumps_route:
        fuel = x[0]
        distance_to_next_pump = x[1]
        tank += fuel

        if distance_to_next_pump > tank:
            break
        else:
            tank -= distance_to_next_pump

    else:
        print(attempt)
        break
    pumps_route.rotate(-1)

