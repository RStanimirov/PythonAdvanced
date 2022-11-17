from collections import deque

materials = [int(el) for el in input().split()]
magic = deque([int(el) for el in input().split()])
archive = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
crafted_presents = {}

while materials and magic:
    last_box = materials[-1]
    first_magic = magic[0]
    total_magic = first_magic * last_box
    if first_magic == 0:
        magic.popleft()

    if last_box == 0:
        materials.pop()

    if total_magic in archive.keys():
        materials.pop()
        magic.popleft()
        toy_crafted = archive[total_magic]
        if toy_crafted not in crafted_presents.keys():
            crafted_presents[toy_crafted] = 0
        crafted_presents[toy_crafted] += 1
    else:
        if total_magic < 0:
            materials.pop()
            magic.popleft()
            new_box = first_magic + last_box
            materials.append(new_box)
        elif total_magic > 0:
            magic.popleft()
            materials[-1] += 15

if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    mat = ", ".join([str(x) for x in reversed(materials)])
    print(f"Materials left: {mat}")
if magic:
    mag = ", ".join([str(x) for x in magic])
    print(f"Magic left: {mag}")

sor_crafted = sorted(crafted_presents.items(), key=lambda x: x[0])
for toy_name, amount in sor_crafted:
    print(f"{toy_name}: {amount}")
