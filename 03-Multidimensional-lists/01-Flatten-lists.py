sub_lists = input().split('|')
# print(sub_lists)
result = []

while sub_lists:
    sublist = sub_lists.pop().split()
    for x in sublist:
        result.append(x)

# print(result)
# print(*result, sep=' ')
print(' '.join([str(x) for x in result]))


