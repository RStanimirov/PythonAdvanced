numbers = [float(x) for x in input().split()]
dict = {}
for x in numbers:
    if x not in dict:
        dict[x] = 0
    dict[x] += 1

for k, v in dict.items():
    print(f"{k} - {v} times")

