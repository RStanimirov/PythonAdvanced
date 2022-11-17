def start_spring(**kwargs):
    result = ''
    result_dict = dict()
    for key, value in kwargs.items():
        if value not in result_dict:
            result_dict[value] = [key]
        else:
            result_dict[value].append(key)
    result_dict = dict(sorted(result_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    for key, value in result_dict.items():
        result += f'{key}:\n'
        for v in sorted(value):
            result += f'-{v}\n'
