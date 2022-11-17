from collections import deque

kids = deque(input().split())
tosses = int(input())

while len(kids) > 1:
    for i in range(1, tosses + 1):
        if i % tosses == 0:
            print(f"Removed {kids.popleft()}")
            break
        kids.append(kids.popleft())
print(f"Last is {''.join(kids)}")
