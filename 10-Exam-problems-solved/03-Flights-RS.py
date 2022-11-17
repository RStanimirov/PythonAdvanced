from collections import deque


def flights(*args):
    flights_dict = {}
    cities = []
    passengers = deque()
    for x in args:
        if type(x) == int:
            passengers.append(x)
        else:
            cities.append(x)
    for x in cities:
        if x == 'Finish':
            break
        else:
            if x not in flights_dict:
                flights_dict[x] = passengers.popleft()
            else:
                flights_dict[x] += passengers.popleft()

    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
