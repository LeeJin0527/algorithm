# 가장 빠른 시간으로 찾는 방법 -> 방문 처리 해야함
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def bfs(n, k):
	q = deque()
	q.append([n, 0])
	count = defaultdict(int)
	while q:
		time, cnt = q.popleft()
		visited[time] = True
		if time == k:
			count[cnt] += 1
		else:
			if 0 <= time+1 < 100001 and not visited[time+1]:
				q.append([time+1, cnt +1])
			if 0 <= time-1 < 100001 and not visited[time-1]:
				q.append([time-1, cnt +1])
			if 0 <= time*2 < 100001 and not visited[time*2]:
				q.append([time*2, cnt +1])
	for key in count.keys():
		print(key)
		print(count[key])
		exit()


n, k = map(int, input().split())
INF = int(1e12)
visited = [False] * 100001
bfs(n,k)