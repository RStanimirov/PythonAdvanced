def start_spring(**kwargs):
    result = ''
    spring_dict = {}
    for k, v in kwargs.items():
        if v not in spring_dict:
            spring_dict[v] = []
        spring_dict[v].append(k)

    for key, value in sorted(spring_dict.items(), key= lambda x: (-len(x[1]), x[1])):
        result += key + ":" + "\n"
        sorted_spring_items = sorted(value)
        result += "\n".join([str(f"-{x}") for x in sorted_spring_items]) + "\n"
    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

