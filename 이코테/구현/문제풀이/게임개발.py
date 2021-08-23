n, m = map(int, input().split())
x, y, direction = map(int, input().split())
data = []

for i in range(n):
	data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = [[0]* m for _ in range(n)]
d[x][y] = 1
def turn_left():
	global direction
	direction -= 1
	if direction == -1:
		direction = 3
count = 1
turn_time = 0
while True:
	turn_left()
	nx = x + dx[direction]
	ny = y + dy[direction]
	if d[nx][ny] == 0 and data[nx][ny] == 0 :
		d[nx][ny] = 1
		count += 1
		x, y = nx, ny
		turn_time = 0
	else:
		turn_time += 1

	if turn_time == 4:
		nx = x - dx[direction]
		ny = y - dy[direction]
		if data[nx][ny] == 0:
			x, y = nx, ny
		else:
			break
		turn_time = 0

print(count)

