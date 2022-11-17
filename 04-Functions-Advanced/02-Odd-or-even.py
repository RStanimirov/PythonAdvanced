command = input()
numbers = [int(x) for x in input().split()]

odd_nums = []
even_nums = []
result = 0

for x in numbers:
    if x % 2 == 0:
        even_nums.append(x)
    else:
        odd_nums.append(x)

if command == "Odd":
    result = sum(odd_nums) * len(numbers)
elif command == "Even":
    result = sum(even_nums) * len(numbers)

print(result)
