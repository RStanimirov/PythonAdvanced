# RS notes added:
from collections import deque
# The number of gas stations in the area. The driver must visit each in a circle:
n = int(input())
gas_queue = deque()
# Loop through each station data to obtain the values for fuel and distance:
for i in range(n):
    pump_data = [int(x) for x in input().split()]
    gas_queue.append(pump_data)
# Now, it's time to make the attempts in order to define from which nearest station to start the journey.
# In this solution of the task, the attempts sequence is linear, starting from 0 index till the last index:
for attempt in range(n):
    # By definition, the tank is always empty before the journey:
    tank = 0
    # Let's declare a flag, so that we can easily print the result:
    failed_attempt = False

    for x in gas_queue:
        fuel = int(x[0])
        distance = int(x[1])
        tank += fuel
        if distance <= tank:
            failed_attempt = False
            tank -= distance
        else:
            failed_attempt = True
            break

    if failed_attempt:
        # gas_queue.append(pumps.popleft())
        gas_queue.rotate(-1)
    else:
        print(attempt)
        quit()