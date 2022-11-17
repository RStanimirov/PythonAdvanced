n = int(input())

odd = set()
even = set()
ascii_val = 0
ascii_val_divided = 0

names = []
for i in range(1, n+1):
    name_data = input()
    for x in name_data:
        ascii_val += int(ord(x))
    ascii_val_divided = int(ascii_val / i)
    names.append(ascii_val_divided)
    ascii_val = 0

for x in names:
    if x % 2 == 0:
        even.add(x)
    else:
        odd.add(x)

even_sum = sum(even)
odd_sum = sum(odd)

if even_sum == odd_sum:
    result = odd.union(even)
elif odd_sum > even_sum:
    result = odd.difference(even)
else:
    result = odd.symmetric_difference(even)

print(*result, sep=', ') #print all elements of the result separated by comma


