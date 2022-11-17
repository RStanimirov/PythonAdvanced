from collections import deque

food_qty = int(input())
orders_list = [int(x) for x in input().split()]
orders_queue = deque(orders_list)
max_order = max(orders_queue)
sum_all_orders = sum(orders_list)

print(max_order)

while orders_queue:
    current_order = orders_queue[0]
    if current_order > food_qty:
        break
    else:
        food_qty -= current_order
        orders_queue.popleft()

# if orders_queue:
#     print(f"Orders left: {' '.join(str(x) for x in orders_queue)}")
# else:
#     print("Orders complete")

if len(orders_queue) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(x) for x in orders_queue)}")

