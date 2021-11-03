INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
	for j in range(1, n+1):
		if i == j:
			graph[i][j] = 0
for i in range(m):
	a, b , c = map(int, input().split())
	graph[a][b] = c
for k in range(1, n+1):
	for x in range(1, n+1):
		for y in range(1, n+1):
			graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])
for i in range(1, n+1):
	for j in range(1, n+1):
		if graph[i][j] == INF:
			print('INF', end = ' ')
		else:
			print(graph[i][j], end = ' ')
	print()

