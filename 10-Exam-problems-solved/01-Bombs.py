from collections import deque

bomb_effect = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

bomb_dict = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
collected_explosives = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
is_pouch_complete = False
# sum_v = 0

while bomb_effect and bomb_casings:
    current_effect = bomb_effect[0]
    current_casing = bomb_casings[-1]
    result = current_effect + current_casing
    if result not in bomb_dict.keys():
        bomb_casings[-1] -= 5
    else:
        bomb_effect.popleft()
        bomb_casings.pop()
        explosive_created = bomb_dict[result]
        collected_explosives[explosive_created] += 1
        # is_pouch_complete = all(value == 3 for value in collected_explosives.values()) # this logic does not take 100 points !
        # if is_pouch_complete:
        #     break
        # try with the following logic -- min(bombs.values()) < 3
        if collected_explosives['Datura Bombs'] >= 3 and collected_explosives['Cherry Bombs'] >= 3 and collected_explosives['Smoke Decoy Bombs'] >= 3:
            is_pouch_complete = True
            break

# print(collected_explosives)
if is_pouch_complete:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effect)}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")

sorted_collection = dict(sorted(collected_explosives.items(), key= lambda x: x[0]))
for k, v in sorted_collection.items():
    print(f"{k}: {v}")