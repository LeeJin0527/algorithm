from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001
count = defaultdict(int)
def bfs(a):
	q = deque()
	q.append([a, 0])
	while q:
		x, cnt = q.popleft()
		visited[x] = True
		if x == k:
			count[cnt] += 1
		else:
			if 0 <= x+1 < 100001 and not visited[x+1]:
				q.append([x+1, cnt+1])
			if 0 <= x-1 < 100001 and not visited[x-1]:
				q.append([x-1, cnt+1])
			if 0 <= x*2 < 100001 and not visited[x*2]:
				q.append([x*2, cnt])

	print(min(count))






bfs(n)