#RS solution 80/100
def operate(sign, *args):
    result = None
    if sign == '+':
        result = 0
        for x in args:
            result += x
    elif sign == '-':
        result = args[0]
        for x in args[1:]:
            result -= x
    elif sign == '*':
        result = args[0]
        for x in args[1:]:
            result *= x
    elif sign == '/':
        result = args[0]
        for x in args[1:]:
            result /= x

    return result


print(operate("+", 1, 1, 1))