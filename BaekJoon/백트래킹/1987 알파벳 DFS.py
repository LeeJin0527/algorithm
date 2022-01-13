import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(sys.stdin.readline().rstrip()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = -1
def dfs(x, y, cnt):
	global result
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if nx < 0 or ny < 0 or nx >= n or ny >= m:
			continue
		if not visited[ord(graph[nx][ny])-65]:
			visited[ord(graph[nx][ny])-65] = True
			dfs(nx, ny, cnt+1)
			visited[ord(graph[nx][ny])-65] = False
		result = max(result, cnt)
	return result

# 알파벳 방문했나요?
visited = [0] * 27
visited[ord(graph[0][0])-65] = True
print(dfs(0, 0, 1))