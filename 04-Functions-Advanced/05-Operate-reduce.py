from functools import reduce


def operate(opr, *args):
    result = None
    if opr == "+":
        result = reduce(lambda x, y: x + y, args)
    elif opr == "-":
        result = reduce(lambda x, y: x - y, args)
    elif opr == "*":
        result = reduce(lambda x, y: x * y, args)
    else:
        result = reduce(lambda x, y: x / y, args)
    return result


print(operate("/", 10, 2, 2))