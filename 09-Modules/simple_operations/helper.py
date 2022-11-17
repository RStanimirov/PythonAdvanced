def sum_nums(a, b):
    return a + b


def sub_nums(a, b):
    return a - b


def multiply_nums(a, b):
    return a * b


def divide_nums(a, b):
    return a / b


def pow_nums(a, b):
    return a ** b


operation_mapper = {"+": sum_nums,
                    "-": sub_nums,
                    "*": multiply_nums,
                    "/": divide_nums,
                    "**": pow_nums}