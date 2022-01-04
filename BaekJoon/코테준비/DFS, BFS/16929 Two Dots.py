import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
cycle = False
for i in range(n):
	graph.append(list(map(str, sys.stdin.readline().rstrip())))
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(start_x, start_y, tmp_x, tmp_y, cnt):
	global cycle
	if cycle:
		return
	visited[tmp_x][tmp_y] = True
	if start_x == tmp_x and start_y == tmp_y and cnt >= 4:
		cycle = True
		return

	for i in range(4):
		nx = tmp_x + dx[i]
		ny = tmp_y + dy[i]
		if nx < 0 or ny < 0 or nx >= n or ny >= m:
			continue
		if not visited[nx][ny] and graph[tmp_x][tmp_y] == graph[nx][ny]:
			dfs(start_x, start_y, nx, ny, cnt+1)
		if nx == start_x and ny == start_y and cnt >= 4:
			dfs(start_x, start_y, nx, ny, cnt)






for i in range(n):
	for j in range(m):
		visited = [[False]* m for _ in range(n)]
		dfs(i, j, i, j, 1)
if cycle:
	print('Yes')
else:
	print('No')