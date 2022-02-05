import sys
import pdb
input = sys.stdin.readline
n, m = map(int, input().split())
# 장애물 수
k = int(input())
# 이동할 판
lst = [[0]*m for _ in range(n)]
# 장애물에는 1 표시
for i in range(k):
	x, y = map(int, input().split())
	lst[x][y] = 1
# 로봇의 시작 위치
a, b = map(int, input().split())
lst[a][b] = 1

# 1 상 2 하 3 좌 4 우
move = list(map(int, input().split()))
for i in range(len(move)):
	move[i] -= 1

# 1 2 3 4 1은 위 방향, 2은 아래 방향, 3은 왼쪽 방향, 4는 오른쪽 방향을
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = a, b
# 한칸도 이동하지 않을때 까지
while True:
	moved = False
	for i in range(len(move)):
		# 로봇은 특정 방향에서 벽을 만날때 까지 한 방향으로 이동

		while True:
			# 이동 할 수 있는 만큼 이동
			nx = x + dx[move[i]]
			ny = y + dy[move[i]]
			# 벽을 만나면 멈춤
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				break
			# 이미 방문 했으면 멈춤
			if lst[nx][ny] == 1:
				break

			# 그게 아니면 계속 이동하고 이동 처리
			if lst[nx][ny] == 0:

				moved = True
				lst[nx][ny] = 1
				x = nx
				y = ny
	# 한칸도 이동하지 않았으면 종료
	if (moved == False):
		break

print(x, y)





