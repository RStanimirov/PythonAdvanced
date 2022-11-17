entries, sub_entries = [int(x) for x in input().split()]

for i in range(entries):
    for j in range(sub_entries):
        print(f"{chr(97 + i)}{chr(97 + i + j)}{chr(97 + i)}", end=' ')
    print()

