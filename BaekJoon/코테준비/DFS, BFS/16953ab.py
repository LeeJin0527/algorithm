from collections import deque
a, b = map(int, input().split())


dx = [2, 1]
def bfs(start):
    cnt = 1
    q = deque()
    q.append([start, cnt])

    while q:
        x, cnt = q.popleft()
        if x == b:
            return cnt
        for i in range(2):
            if i == 0:
                nx = x * 2
            else:
                nx = int(str(x)+str(1))
            if nx < 0 or nx > b:
                continue
            q.append((nx, cnt+1))
    return -1

print(bfs(a))
