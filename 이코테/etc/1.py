n = int(input())
go = list(input().split())

move_types = ['R', 'L', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
x = 1
y = 1
for i in go:
	for j in range(4):
		if i == move_types[j]:
			nx = x + dx[j]
			ny = y + dy[j]

	if nx < 1 or ny < 1 or nx > n or ny > n:
		continue
	x, y = nx , ny
print(x, y)
