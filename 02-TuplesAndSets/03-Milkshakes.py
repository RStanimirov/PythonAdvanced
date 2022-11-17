from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milk_cups = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolates and milk_cups and milkshakes < 5:
    current_chocolate = chocolates.pop()
    current_milk_cup = milk_cups.popleft()

    if current_chocolate <= 0 and current_milk_cup <= 0:
        continue
    elif current_chocolate <= 0:
        milk_cups.appendleft(current_milk_cup)
        continue
    elif current_milk_cup <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_milk_cup:
        milkshakes += 1
    else:
        chocolates.append(current_chocolate - 5)
        milk_cups.append(current_milk_cup)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
else:
    print("Milk: empty")