n = int(input())
unique_names = set()
for i in range(n):
    name = input()
    unique_names.add(name)
for person in unique_names:
    print(person)
