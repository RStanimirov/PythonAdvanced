def math_operations(*args, **keywords):
    from collections import deque
    int_list = deque(args)
    keys_dict = deque(keywords.keys())
    actions = deque(["+", "-", "/", "*"])
    while int_list:
        element = int_list.popleft()
        act = actions[0]
        key = keys_dict[0]
        if act == "+":
            keywords[key] += element
        elif act == "-":
            keywords[key] -= element
        elif act == "/":
            if element != 0:
                keywords[key] /= element
        elif act == "*":
            keywords[key] *= element

        actions.rotate(-1)
        keys_dict.rotate(-1)

    return keywords


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))