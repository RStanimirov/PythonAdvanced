n = int(input())

guests = set()

for i in range(n):
    code = input()
    guests.add(code)

command = input()

while command != "END":
    guests.remove(command)
    command = input()

print(len(guests))
print('\n'.join(sorted(guests)))

