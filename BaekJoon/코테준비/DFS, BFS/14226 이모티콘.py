from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
q.append([1, 0])
MAX_SIZE = 1001
visited = [[-1] *MAX_SIZE for _ in range(MAX_SIZE)]
visited[1][0] = 0
while q:
	s, c = q.popleft()
	if visited[s][s] == -1:
		visited[s][s] = visited[s][c] + 1
		q.append((s, s))
	if s+c < MAX_SIZE and visited[s+c][c] == -1:
		visited[s+c][c] = visited[s][c] + 1
		q.append((s+c, c))
	if s-1 >= 1 and visited[s-1][c] == -1:
		visited[s-1][c] = visited[s][c] +1
		q.append((s-1, c))
answer = -1
for i in range(n+1):
	if visited[n][i] != -1:
		if answer == -1 or answer > visited[n][i]:
			answer = visited[n][i]
print(answer)