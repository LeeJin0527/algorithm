from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()
queue.append(5)
queue.append(6)
queue.append(4)
queue.append(2)
queue.popleft()
queue.append(1)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
print(list(queue))
