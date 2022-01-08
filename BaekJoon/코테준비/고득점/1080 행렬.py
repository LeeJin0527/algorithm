import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lstA = []
lstB = []
for i in range(n):
	lstA.append(list(map(int, sys.stdin.readline().rstrip())))
for i in range(n):
	lstB.append(list(map(int, sys.stdin.readline().rstrip())))
def matrix(i, j):
	for x in range(i, i+3):
		for y in range(j, j+3):
			lstA[x][y] = 1 - lstA[x][y]
count = 0
for i in range(n-2):
	for j in range(m-2):
		if lstA[i][j] != lstB[i][j]:
			matrix(i, j)
			count += 1

flag = 0
for i in range(n):
	for j in range(m):
		if lstA[i][j] != lstB[i][j]:
			flag = 1
			break
if flag == 1:
	print(-1)
else:
	print(count)

