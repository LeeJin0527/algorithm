import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
	a, b, c = map(int, input().split())
	if graph[a-1][b-1] > c :
		graph[a-1][b-1] = c
for k in range(n):
	for x in range(n):
		for y in range(n):
			if x != y and graph[x][y] > graph[x][k] + graph[k][y]:
				graph[x][y] = graph[x][k] + graph[k][y]
for i in range(n):
	for j in range(n):
		if graph[i][j] == INF :
			print(0, end = ' ')
		else:
			print(graph[i][j], end = ' ')
	print()
