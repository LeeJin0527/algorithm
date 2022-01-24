from collections import deque
t = int(input())
def bfs(x, y):
	q = deque()
	q.append([x, y])
	visited = []
	while q:
		x, y = q.popleft()
		if x == end_x and y == end_y:
			print('happy')
			return
		for pos in conv:
			if abs(x - pos[0]) + abs(y - pos[1]) <= 1000 and pos not in visited:
				q.append([pos[0], pos[1]])
				visited.append([pos[0], pos[1]])
	print('sad')

for i in range(t):
	n = int(input())
	start_x, start_y = map(int, input().split())
	conv = []
	for i in range(n):
		a, b = map(int, input().split())
		conv.append([a, b])
	end_x, end_y = map(int, input().split())
	conv.append([end_x, end_y])
	bfs(start_x, start_y)