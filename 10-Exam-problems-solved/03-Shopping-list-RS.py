def shopping_list(budget, **kwargs):
    counter = 0
    shoppimg_cart = []
    if budget < 100:
        return "You do not have enough budget."
    else:
        for k, v in kwargs.items():
            price = float(v[0])
            qty = int(v[1])
            total_amount_per_item = price * qty
            if total_amount_per_item <= budget:
                budget -= total_amount_per_item
                counter += 1
                shoppimg_cart.append(f"You bought {k} for {total_amount_per_item:.2f} leva.")
                if counter == 5:
                    break
        return '\n'.join(shoppimg_cart)

# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
