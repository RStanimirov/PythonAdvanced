# RS correct output but judge zero points:
def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for x in args:
        # command = x[0]
        arguments = x[1]
        if sum_numbers in x:
            func_result = sum_numbers(*arguments)
            result.append(func_result)
        elif multiply_numbers in x:
            func_result = multiply_numbers(*arguments)
            result.append(func_result)
    return result


print(func_executor((multiply_numbers, (2, 4)), (sum_numbers, (1, 2))))
