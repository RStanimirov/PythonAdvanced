def flights(*args):
    destinations = {}
    for i, arg in enumerate(args):
        if arg == "Finish":
            break
        if i % 2 == 0:
            if arg not in destinations:
                destinations[arg] = 0
            destinations[arg] += args[i + 1]
    return destinations


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
