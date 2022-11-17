#RS tried something different but only 75% in Judge:
parentheses_input = input()

if len(parentheses_input) <= 1:
    print("NO")
    quit()
if len(parentheses_input) % 2 != 0:
    print("NO")
    quit()
if parentheses_input[0] in ')}]' or parentheses_input[-1] in '({[':
    print("NO")
    quit()

parentheses_expression_half = int(len(parentheses_input)/2)

first_half_input = ''
second_half_input = ''
round_pair = "()"
curly_pair = "{}"
square_pair = "[]"

for i in range(0, parentheses_expression_half):
    first_half_input += parentheses_input[i]

for idx in range(parentheses_expression_half, len(parentheses_input)):
    second_half_input += parentheses_input[idx]

if first_half_input[-1] + second_half_input[0] == round_pair or first_half_input[-1] + second_half_input[0] == curly_pair or first_half_input[-1] + second_half_input[0] == square_pair:
    print("YES")
else:
    print("NO")





