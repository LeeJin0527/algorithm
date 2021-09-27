from collections import deque

queue = deque()
queue.append(1)
queue.append(3)
queue.append(2)
queue.popleft()
queue.append(7)
queue.popleft()

print(list(queue))
queue.reverse()
print(list(queue))