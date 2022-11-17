def age_assignment(*args, **kwargs):
    result_dict = {}
    name_list = []

    for x in args:
        x = x.strip('"')
        name_list.append(x)
    for name in name_list:
        first_char = name[0]
        for k, v in kwargs.items():
            if k == first_char:
                result_dict[name] = kwargs[k]
    return result_dict


print(age_assignment("Peter", "George", G=26, P=19))