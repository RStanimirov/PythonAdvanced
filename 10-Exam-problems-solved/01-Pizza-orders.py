from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
employees_capacity = [int(x) for x in input().split(', ')]
# Your task is to check if all pizza orders are completed.
# To do that, you should take the first order and the last employee
prepared_pizzas = []
is_order_completed = False
while pizza_orders and employees_capacity:
    if pizza_orders[0] > 10 or pizza_orders[0] <= 0:
        pizza_orders.popleft()
    else:
        if pizza_orders[0] <= employees_capacity[-1]:
            is_order_completed = True
            prepared_pizzas.append(pizza_orders[0])
            pizza_orders.popleft()
            employees_capacity.pop()
        elif pizza_orders[0] > employees_capacity[-1]:
            pizza_orders[0] = pizza_orders[0] - employees_capacity[-1]
            prepared_pizzas.append(employees_capacity.pop())

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {sum(prepared_pizzas)}")
    print(f"Employees: {', '.join(str(x) for x in employees_capacity)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")

