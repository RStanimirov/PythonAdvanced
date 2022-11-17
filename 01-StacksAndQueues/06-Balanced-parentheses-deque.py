from collections import deque

parentheses_input = list(input())
open_parentheses = deque()
fail_flag = 0

if len(parentheses_input) == 0:
    fail_flag = 1

for i in range(len(parentheses_input)):
    if parentheses_input[i] in "{[(":
        open_parentheses.append(parentheses_input[i])
    elif parentheses_input[i] in "}])":
        if len(open_parentheses) > 0:
            open_bracket = open_parentheses.pop()
            if f'{open_bracket}{parentheses_input[i]}' in ['()', '{}', '[]']:
                continue
            else:
                fail_flag = 1
                break
        else:
            fail_flag = 1
            break

if fail_flag or len(open_parentheses) > 0:
    print("NO")
else:
    print("YES")