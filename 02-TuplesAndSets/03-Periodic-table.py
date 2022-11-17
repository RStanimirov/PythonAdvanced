n = int(input())
chemicals_set = set()
for i in range(n):
    chemical_data = input().split()
    for x in chemical_data:
        chemicals_set.add(x)

print('\n'.join(chemicals_set))