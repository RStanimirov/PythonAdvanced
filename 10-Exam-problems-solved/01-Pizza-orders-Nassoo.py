from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))
employees = deque(int(x) for x in input().split(', '))

total_pizzas = 0
while pizza_orders and employees:
    order = pizza_orders.popleft()
    employee = employees.pop()

    if order <= 0 or order > 10:
        employees.append(employee)
        continue

    total_pizzas += min(employee, order)

    if order > employee:
        order -= employee
        pizza_orders.appendleft(order)

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(el) for el in pizza_orders)}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(el) for el in employees)}")