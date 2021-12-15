# brute-force
import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
	lst.append(list(sys.stdin.readline().rstrip()))
# print(lst)
def serial_cnt(lst):
	cnt = 0
	for i in range(n):
		rowCnt = 1
		colCnt = 1
		for j in range(n-1):
			if lst[i][j] == lst[i][j+1]:
				rowCnt += 1
			else:
				cnt = max(cnt, rowCnt)
				rowCnt = 1
			if lst[j][i] == lst[j+1][i]:
				colCnt += 1
			else:
				cnt = max(cnt, colCnt)
				colCnt = 1
		cnt = max(cnt, rowCnt, colCnt)
	return cnt



dx = [1, 0]
dy = [0, -1]
answer = 0
for i in range(n):
	for j in range(n):
		for k in range(2):
			nx = i + dx[k]
			ny = j + dy[k]
			if nx >= n or ny >= n:
				continue
			elif lst[i][j] == lst[nx][ny]:
				continue
			# swap
			elif lst[i][j] != lst[nx][ny]:
				lst[i][j], lst[nx][ny] = lst[nx][ny], lst[i][j]
				# serial_cnt
				answer = max(answer, serial_cnt(lst))
				lst[i][j], lst[nx][ny] = lst[nx][ny], lst[i][j]
print(answer)


