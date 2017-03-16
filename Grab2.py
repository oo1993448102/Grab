from collections import deque

list = [1, 2, 3]
queue = deque(list)
queue.append(4)
print(queue.popleft())
print(queue)
