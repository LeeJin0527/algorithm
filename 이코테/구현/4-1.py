# N 입력 받기
N = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 방향이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
	for i in range(len(move_types)):
		if plan == move_types[i]:
			nx = x + dx[i]
			ny = y + dy[i]
	if nx < 1 or ny < 1 or nx > N or ny > N:
		continue
	x, y = nx, ny
print(x, y)
