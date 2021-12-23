# N, M을 공백으로 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]

# 현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
x, y, direction = map ( int, input().split())
d[x][y] = 1 #현재 좌표 방문처리

# 전체 맵 정보를 입력받기
array =[]
for i in range(n):
	array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
	global direction
	direction -=1
	if direction == -1:
		direction = 3
count = 1
turn_time = 0
while True:
	turn_left()
	nx = x + dx[direction]
	ny = y + dy[direction]
	# 빙문 하지 않았고 방문 할 수 있는 곳
	if d[nx][ny] == 0 and array[nx][ny] == 0:
		# 방문 처리 하고 이동
		d[nx][ny] = 1
		x = nx
		y = ny
		count += 1
		turn_time = 0
		continue
	else:
		turn_time += 1

	if turn_time == 4:
		nx = x - dx[direction]
		ny = y - dy[direction]

		if array[nx][ny] == 0:
			x = nx
			y = ny
		else:
			break
		turn_time = 0
print(count)
 
