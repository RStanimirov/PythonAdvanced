parenthesis_input = input()

list_char = []
opening = ["(", "{", "["]
closing = [")", "}", "]"]

if len(parenthesis_input) % 2 == 0:  # Може да се добави и "and parenthesis_input[0] in opening"
    # към провеката и да се провери дали не почва със затваряща скоба

    for x in parenthesis_input:
        if x in opening:
            list_char.append(opening.index(x))
        elif x in closing:
            index = closing.index(x)
            if index == list_char[-1]:
                list_char.pop()
            else:
                break
    if len(list_char) == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")