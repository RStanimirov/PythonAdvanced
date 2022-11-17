from collections import deque
chocolates = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])
counter_shakes = 0
is_milkshakes = False

while chocolates and milk:
    current_choc = chocolates[-1]
    current_milk = milk[0]
    if current_choc <= 0 or current_milk <= 0:
        if current_milk <= 0:
            milk.popleft()
        if current_choc <= 0:
            chocolates.pop()
    else:
        if current_choc == current_milk:
            counter_shakes += 1
            chocolates.pop()
            milk.popleft()
        else:
            milk.rotate(-1)
            # milk.append(milk.popleft())
            chocolates[-1] -= 5
        if counter_shakes >= 5:
            is_milkshakes = True
            break

if is_milkshakes:
    print("Great! You made all the chocolate milkshakes needed!")
    if chocolates:
        print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
    else:
        print("Chocolate: empty")
    if milk:
        print(f"Milk: {', '.join(str(x) for x in milk)}")
    else:
        print("Milk: empty")
else:
    print("Not enough milkshakes.")
    if chocolates:
        print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
    else:
        print("Chocolate: empty")
    if milk:
        print(f"Milk: {', '.join(str(x) for x in milk)}")
    else:
        print("Milk: empty")