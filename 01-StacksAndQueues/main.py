from collections import deque

name = input()
name_queue = deque()

while name != "end":
    name_queue.append(name)
    name = input()

print(name_queue)

name_queue.append("Jannet")
name_queue.appendleft("Johny")
name_queue.popleft()

print(name_queue)
print(name_queue.popleft())
print(name_queue)
