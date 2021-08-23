n = int(input())
data = list(input().split())
# [R R R U D D]
direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x = 1
y = 1

for d in data:
	for i, dir in enumerate(direction):
		if d == dir:
			nx = x + dx[i]
			ny = y + dy[i]

	if nx < 1 or ny < 1 or nx > n or ny > n:
		continue
	x, y = nx, ny


print(x, y)

