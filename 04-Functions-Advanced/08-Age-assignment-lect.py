def age_assignment(*args, **kwargs):
    result_dict = {}
    for x in args:
        name = x
        first_letter = name[0]
        age = kwargs[first_letter]
        result_dict[name] = age

    return result_dict


print(age_assignment("Peter", "George", G=26, P=19))