import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(sys.stdin.readline().rstrip()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
	result = 1
	q = set([(0, 0, graph[0][0])])
	while q:
		x, y, visit = q.pop()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				continue
			if graph[nx][ny] not in visit:
				q.add((nx, ny, visit+graph[nx][ny]))
				result = max(result, len(visit+graph[nx][ny]))
	return result

print(bfs())