n = int(input())

cars_parked = set()

for i in range(n):
    car_data = input().split(', ')
    command = car_data[0]
    car = car_data[1]
    if command == "IN":
        cars_parked.add(car)
    else:
        cars_parked.remove(car)

if cars_parked:
    print('\n'.join(cars_parked))
else:
    print("Parking Lot is Empty")