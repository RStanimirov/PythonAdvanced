#RS modelled on other solutons finally 100/100 :
from collections import deque
materials_for_crafting = [int(x) for x in input().split()]
magic_powers = deque([int(x) for x in input().split()])
presents_model_dict = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
crafted_gifts = {}

while materials_for_crafting and magic_powers:
    current_material = materials_for_crafting[-1]
    current_magic = magic_powers[0]
    if current_material == 0 or current_magic == 0:
        if current_material == 0:
            materials_for_crafting.pop()
        if current_magic == 0:
            magic_powers.popleft()
    else:
        total_magic = current_material * current_magic
        if total_magic in presents_model_dict:
            materials_for_crafting.pop()
            magic_powers.popleft()
            toy_crafted = presents_model_dict[total_magic]
            if toy_crafted not in crafted_gifts:
                crafted_gifts[toy_crafted] = 0
            crafted_gifts[toy_crafted] += 1
        else:
            if total_magic < 0:
                materials_for_crafting.pop()
                magic_powers.popleft()
                blended_value = current_material + current_magic
                materials_for_crafting.append(blended_value)
            elif total_magic > 0:
                magic_powers.popleft()
                materials_for_crafting[-1] += 15

if 'Doll' in crafted_gifts and 'Wooden train' in crafted_gifts:
    print('The presents are crafted! Merry Christmas!')
elif 'Teddy bear' in crafted_gifts and 'Bicycle' in crafted_gifts:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials_for_crafting:
    print(f'Materials left: {", ".join(str(i) for i in reversed(materials_for_crafting))}')
if magic_powers:
    print(f'Magic left: {", ".join(str(i) for i in magic_powers)}')
sorted_dictionary = sorted(crafted_gifts.items(), key=lambda x: x[0])
for k, v in sorted_dictionary:
    print(f"{k}: {v}")
