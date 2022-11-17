def concatenate(*args):
    result = ''
    for x in args:
        result += x
    return result

print(concatenate("I", " ", "Love", " ", "Python"))