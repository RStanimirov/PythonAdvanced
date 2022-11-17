numbers_list = input().split()

for i in range(len(numbers_list)):
    print(numbers_list.pop(), end=' ')