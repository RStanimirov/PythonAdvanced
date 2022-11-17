# RS solution slightly optimised:
from collections import deque
raw_string = deque(input().split())
main_colours_model = ["red", "yellow", "blue"]
secondary_colours_model = ["orange", "purple", "green"]
colours_main = []
colours_secondary = []
all_colours = []

while raw_string:
    if len(raw_string) == 1:
        left_str = raw_string.popleft()
        right_str = ''
    else:
        left_str = raw_string.popleft()
        right_str = raw_string.pop()

    if left_str+right_str in main_colours_model or left_str+right_str in secondary_colours_model:
        all_colours.append(left_str+right_str)
        for x in all_colours:
            if x in main_colours_model:
                colours_main.append(x)
            else:
                colours_secondary.append(x)
    elif right_str+left_str in main_colours_model or right_str+left_str in secondary_colours_model:
        all_colours.append(right_str+left_str)
        for x in all_colours:
            if x in main_colours_model:
                colours_main.append(x)
            else:
                colours_secondary.append(x)
    else:
        left_str = left_str[0:len(left_str)-1]
        right_str = right_str[0:len(right_str)-1]
        if left_str:
            raw_string.insert(len(raw_string)//2, left_str)
        if right_str:
            raw_string.insert(len(raw_string)//2, right_str)

secondary_formation_dict = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue'],
}

all_colours_print = []

for x in all_colours:
    if x in colours_main:
        all_colours_print.append(x)
    else:
        for k, v in secondary_formation_dict.items():
            if k == x:
                contains_secondary = all([el in colours_main for el in v])
                if contains_secondary:
                    all_colours_print.append(k)

print(all_colours_print)