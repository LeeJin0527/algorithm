# BFS 돌려서 4개 영역의 합이 최대인 것 구하기
import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
input = sys.stdin.readline
n, m = map(int, input().split())
lst = []
maxValue = 0
for i in range(n):
	lst.append(list(map(int, input().split())))

def dfs(x, y, cur,  cnt):
	global maxValue
	if cnt == 4:
		maxValue = max(maxValue, cur)
		return

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if nx < 0 or ny < 0 or nx >= n or ny >= m:
			continue
		if not visited[nx][ny]:
			visited[nx][ny] = True
			dfs(nx, ny, cur + lst[nx][ny], cnt +1)
			visited[nx][ny] = False
def weird(x, y):
	global maxValue
	for i in range(4):
		tmp = lst[x][y]
		for j in range(3):
			t = (i + j) % 4
			nx = x + dx[t]
			ny = y + dy[t]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				tmp = 0
				break
			tmp += lst[nx][ny]
		maxValue = max(maxValue, tmp)
visited = [[False]*m for _ in range(n)]
for i in range(n):
	for j in range(m):
		visited[i][j] = True
		dfs(i, j, lst[i][j],  1)
		visited[i][j] = False
		weird(i, j)

print(maxValue)
