equation = input()

brackets_idx_list = []

for i in range(len(equation)):
    if equation[i] == "(":
        brackets_idx_list.append(i)
    elif equation[i] == ")":
        opening_bracket_idx = brackets_idx_list.pop()
        closing_bracket_idx = i
        print(equation[opening_bracket_idx:closing_bracket_idx + 1])
