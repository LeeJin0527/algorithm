from collections import deque, defaultdict
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
def bfs(n, k):
	q = deque()
	q.append([n, 0])
	while q:
		time, cnt = q.popleft()
		visited[time] = True
		path[cnt].append(time)
		if time == k:
			print(cnt)
			break
		else:
			if 0 <= time +1 < 100001 and not visited[time+1]:
				q.append([time+1, cnt+1])
			if 0 <= time -1 < 100001 and not visited[time-1]:
				q.append([time-1, cnt+1])
			if 0 <= time *2 < 100001 and not visited[time*2]:
				q.append([time*2, cnt+1])
	result = []
	result.append(k)
	tmp = k
	for i in range(cnt-1, 0, -1):
		if tmp / 2 in path[i] :
			result.append(int(tmp/2))
			tmp = int(tmp / 2)
		elif tmp -1 in path[i] :
			result.append(tmp-1)
			tmp = tmp-1
		elif tmp +1 in path[i] :
			result.append(tmp+1)
			tmp = tmp+1
	result.append(n)
	if n == k:
		print(k)
	else:
		print(" ".join(map(str, result[::-1])))

visited = [False] * 100001
path = defaultdict(list)
counted = defaultdict(int)
bfs(n, k)