from collections import deque

input_str_to_list = input().split()
step = int(input())
players = deque(input_str_to_list)
i = 1

while len(players) > 1:
    kid = players.popleft()

    if step == i:
        print(f'Removed {kid}')
        i = 0
    else:
        players.append(kid)
    i += 1

print(f'Last is {players.pop()}')