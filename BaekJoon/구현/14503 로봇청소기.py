import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c , direction = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))
visited = [[False]*m for _ in range(n)]
visited[r][c] = True
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def turn_left():
	global direction
	direction -= 1
	if direction == -1:
		direction = 3
turn_time = 0
cnt = 1

while True:
	turn_left()
	nx = r + dx[direction]
	ny = c + dy[direction]
	if graph[nx][ny] == 0 and not visited[nx][ny]:
		visited[nx][ny] = True
		r = nx
		c = ny
		cnt += 1
		turn_time = 0
		continue
	else:
		turn_time += 1
	if turn_time == 4:
		nx = r - dx[direction]
		ny = c - dy[direction]
		if graph[nx][ny] == 0:
			visited[nx][ny] = True
			r = nx
			c = ny

		else:
			break
		turn_time = 0
print(cnt)