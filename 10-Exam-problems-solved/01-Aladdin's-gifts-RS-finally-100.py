# RS initially 83/100 however after mentorship advised a correction at line 79, 100/100:
from collections import deque
materials_ints = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])
crafted_gifts = {}
new_result = 0

while materials_ints and magic_levels:
    current_material = materials_ints[-1]
    current_magic = magic_levels[0]
    if new_result != 0:
        result = new_result
    else:
        result = current_material + current_magic

    if 100 <= result <= 199:
        crafted_present = 'Gemstone'
        if crafted_present not in crafted_gifts:
            crafted_gifts[crafted_present] = 1
        else:
            crafted_gifts[crafted_present] += 1
        materials_ints.pop()
        magic_levels.popleft()
        new_result = 0

    elif 200 <= result <= 299:
        crafted_present = 'Porcelain Sculpture'
        if crafted_present not in crafted_gifts:
            crafted_gifts[crafted_present] = 1
        else:
            crafted_gifts[crafted_present] += 1
        materials_ints.pop()
        magic_levels.popleft()
        new_result = 0

    elif 300 <= result <= 399:
        crafted_present = 'Gold'
        if crafted_present not in crafted_gifts:
            crafted_gifts[crafted_present] = 1
        else:
            crafted_gifts[crafted_present] += 1
        materials_ints.pop()
        magic_levels.popleft()
        new_result = 0

    elif 400 <= result <= 499:
        crafted_present = 'Diamond Jewellery'
        if crafted_present not in crafted_gifts:
            crafted_gifts[crafted_present] = 1
        else:
            crafted_gifts[crafted_present] += 1
        materials_ints.pop()
        magic_levels.popleft()
        new_result = 0

    if result < 100:
        if result % 2 == 0:
            current_material *= 2
            current_magic *= 3
            new_result = current_material + current_magic
            if new_result >= 100:
                continue
            else:
                materials_ints.pop()
                magic_levels.popleft()
                new_result = 0
        else:
            new_result = result * 2
            if new_result >= 100:
                continue
            else:
                materials_ints.pop()
                magic_levels.popleft()
                new_result = 0

    elif result > 499:
        new_result = result / 2
        if new_result > 499:
            materials_ints.pop()
            magic_levels.popleft()

if ('Gemstone' in crafted_gifts.keys() and 'Porcelain Sculpture' in crafted_gifts.keys()) or \
        ('Gold' in crafted_gifts.keys() and 'Diamond Jewellery' in crafted_gifts.keys()):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials_ints:
    print(f"Materials left: {', '.join(str(x) for x in materials_ints)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")
for k, v in sorted(crafted_gifts.items()):
    print(f"{k}: {v}")
