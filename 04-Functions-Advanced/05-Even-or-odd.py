def even_odd(*args):
    even_nums = []
    odd_nums = []
    param = args[-1]
    string = args[:-1]
    if param == "even":
        for x in string:
            if x % 2 == 0:
                even_nums.append(x)
        return even_nums
    elif param == "odd":
        for x in string:
            if x % 2 != 0:
                odd_nums.append(x)
        return odd_nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))

