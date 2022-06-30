import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = []
for i in range(n):
	lst.append([0] + list(map(int, input().split())))
lst.insert(0, [0] * (n+1))
sumGroup = [[0] * (n+1) for _ in range(n+1)]
sumGroup[1][1] = lst[1][1]

for i in range(n+1):
	for j in range(n+1):
		if i == 0 or j == 0:
			continue
		if i == 1:
			sumGroup[i][j] = sumGroup[i][j-1] + lst[i][j]
		if j == 1:
			sumGroup[i][j] = sumGroup[i-1][j] + lst[i][j]
		else:
			sumGroup[i][j] = sumGroup[i-1][j] + sumGroup[i][j-1] - sumGroup[i-1][j-1] + lst[i][j]


for _ in range(m):
	c, d, a, b = map(int, input().split())
	
	print(sumGroup[a][b] - sumGroup[c-1][b] - sumGroup[a][d-1] + sumGroup[c-1][d-1])
