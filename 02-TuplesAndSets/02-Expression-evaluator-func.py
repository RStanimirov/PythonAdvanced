def addition(operator, list_of_char):
    result = int(operator)
    list_of_char = [int(x) for x in list_of_char]
    for num in list_of_char:
        result += num
    return result


def multiplication(operator, list_of_char):
    result = int(operator)
    list_of_char = [int(x) for x in list_of_char]
    for num in list_of_char:
        result *= num
    return result


def subtraction(operator, list_of_char):
    result = int(operator)
    list_of_char = [int(x) for x in list_of_char]
    for num in list_of_char:
        result -= num
    return result


def division(operator, list_of_char):
    result = int(operator)
    list_of_char = [int(x) for x in list_of_char]
    for num in list_of_char:
        result /= num
    return result


expression = input().split()

symbols = ["+", "*", "-", "/"]

while len(expression) > 1:
    for char in expression:
        if "+" == char:
            index = expression.index(char)
            result = addition(expression[0], expression[1:index])
            del expression[:index + 1]
            expression.insert(0, result)
            break

        elif "*" == char:
            index = expression.index(char)
            result = multiplication(expression[0], expression[1:index])
            del expression[:index + 1]
            expression.insert(0, result)
            break

        elif "-" == char:
            index = expression.index(char)
            result = subtraction(expression[0], expression[1:index])
            del expression[:index + 1]
            expression.insert(0, result)
            break

        elif "/" == char:
            index = expression.index(char)
            result = int(division(expression[0], expression[1:index]))
            del expression[:index + 1]
            expression.insert(0, result)
            break

print(*expression)