def math_operations(*args, **kwargs):
    dictionary = dict(kwargs)
    for i in range(len(args)):
        if i % 4 == 0:
            dictionary['a'] += args[i]
        elif i % 4 == 1:
            dictionary['s'] -= args[i]
        elif i % 4 == 2:
            if not args[i] == 0:
                dictionary['d'] /= args[i]
        else:
            dictionary['m'] *= args[i]
    return dictionary