n, m = map(int, input().split())

dpList = []
for i in range(n):
	dpList.append(list(map(int, input().split())))
k = int(input())

sumList = [[0 for _ in range(m+1)] for _ in range(n+1)]


for i in range(1, n+1):
	for j in range(1, m+1):
		sumList[i][j] = dpList[i-1][j-1] + sumList[i][j-1] + sumList[i-1][j] - sumList[i-1][j-1]
indexList = []
for h in range(k):
	i, j, x, y = map(int, input().split())
	print(sumList[x][y] - sumList[i-1][y] - sumList[x][j-1] + sumList[i-1][j-1])

