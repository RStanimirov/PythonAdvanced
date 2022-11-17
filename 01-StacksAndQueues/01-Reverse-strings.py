# input_as_list = list(input())
# stack = []
#
# for i in range(len(input_as_list)):
#     stack.append(input_as_list.pop())
#
# print("".join(stack))

text = list(input())
rev_text = ''
while text:
    rev_text += text.pop()

print(rev_text)



