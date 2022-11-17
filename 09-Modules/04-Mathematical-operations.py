from simple_operations.helper import operation_mapper

equation = input().split()

a = float(equation[0])
operator = equation[1]
b = float(equation[2])

try:
    print(operation_mapper[operator](a, b))
except ZeroDivisionError:
    print("Invalid calculation - cannot divide by 0.")