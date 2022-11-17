from collections import  deque


def math_operations(*args, **kwargs):
    numbers = deque(args)
    while numbers:
        kwargs['a'] += numbers.popleft()
        if not numbers:
            break
        kwargs['s'] -= numbers.popleft()
        if not numbers:
            break
        divisor = numbers.popleft()
        if divisor != 0:
            kwargs['d'] /= divisor
        if not numbers:
            break
        kwargs['m'] *= numbers.popleft()
        # no need for break-check because after that operation we loop into while cycle above.
    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))