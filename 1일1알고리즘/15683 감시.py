import copy
n, m = map(int, input().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
cctv = []
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
	for j in range(m):
		if 0 < graph[i][j] < 6:
			cctv.append([graph[i][j], i, j])

# cctv가 이동할 수 있는 방향
mode = [[],
       [[0], [1], [2], [3]],
       [[0, 2], [1, 3]],
       [[0, 1], [1, 2], [2, 3], [3, 0]],
       [[0, 1, 2], [1, 2, 3],[2, 3, 0], [3, 0, 1]],
       [[0, 1, 2, 3]]
       ]

def dfs(depth, graph):
	global min_result
	if depth == len(cctv):
		count = 0
		for i in range(n):
			count += graph[i].count(0)
		min_result = min(min_result, count)
		return
	temp = copy.deepcopy(graph)
	cctv_dir, x, y = cctv[depth]
	for each_dir in mode[cctv_dir]:
		# 감시 할 수 있는 방향 모두 표시
		fill(temp, x, y, each_dir)
		# 다음 카메라 방향
		dfs(depth + 1, temp)
		# 다시 복원 
		temp = copy.deepcopy(graph)



def fill(graph, x, y, mn):
	for i in mn:
		nx = x
		ny = y
		# 끝까지 이동 벽 만나거나 범위 벗어나면 종료 , 방문 표시해주기
		while True:
			nx += dx[i]
			ny += dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				break
			if graph[nx][ny] == 6:
				break
			if graph[nx][ny] == 0:
				graph[nx][ny] = 7
min_result = int(1e9)
dfs(0, graph)
print(min_result)