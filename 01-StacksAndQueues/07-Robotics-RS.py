#RS slightly modified lect solution:
from collections import deque


def convert_seconds_to_str_time(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots_data = input().split(';')

robots_dict = {}
busy_time_by_robot = {}
products_queue = deque()
robot_speed = 0

for x in robots_data:
    robot_spec = x.split('-')
    robot_name = robot_spec[0]
    robot_speed = int(robot_spec[1])
    robots_dict[robot_name] = robot_speed
    busy_time_by_robot[robot_name] = -1

time_string = input().split(':')

hours = int(time_string[0])
minutes = int(time_string[1])
seconds = int(time_string[2])
if minutes == 0 or seconds == 0:
    total_seconds = hours * 60 * 60
else:
    total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds

command = input()

while command != "End":
    products_queue.append(command)
    command = input()

while products_queue:
    total_seconds += 1
    current_product = products_queue.popleft()

    for k, v in busy_time_by_robot.items():
        if total_seconds >= v:
            busy_time_by_robot[k] = total_seconds + robots_dict[k]
            print(f"{k} - {current_product} [{convert_seconds_to_str_time(total_seconds)}]")
            break
    else:
        products_queue.append(current_product)


