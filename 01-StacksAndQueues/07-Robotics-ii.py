from collections import deque


def convert_to_string(seconds):
    import time
    return time.strftime("%H:%M:%S", time.gmtime(seconds))


def convert_to_sec(cur_start_time):
    import time
    sec_start_time = cur_start_time[0] * 3600 + cur_start_time[1] * 60 + cur_start_time[2]
    return sec_start_time


robots = []
product_line = deque()
robots_info = input().split(';')
for robot in robots_info:
    robot_info = robot.split('-')
    robot_name, pr_time = robot_info
    robots.append([0, int(pr_time), robot_name])
start_time = input().split(':')
start_time = list(map(int, start_time))
clock_line: int = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]
#

c_product = input()
while c_product != 'End':
    product_line.append(c_product)
    c_product = input()
#
while product_line:
    clock_line += 1
    c_product = product_line.popleft()
    robot_found = False
    for robot in robots:
        if clock_line >= robot[0]:  # current robot is free#
            robot_found = True
            new_time = convert_to_string(clock_line)
            print(f"{robot[2]} - {c_product} [{new_time}]")
            robot[0] = clock_line + robot[1]  # new finish time
            break
    if not robot_found:
        product_line.append(c_product)