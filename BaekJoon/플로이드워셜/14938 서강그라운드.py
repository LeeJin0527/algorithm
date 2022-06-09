import sys
INF = int(1e9)
input = sys.stdin.readline
n, m, r = map(int, input().split())
itemValueList = list(map(int, input().split()))
arr = [[INF] * n for _ in range(n)]
for i in range(r):
	a, b, dist = map(int, input().split())
	arr[a-1][b-1] = min(arr[a-1][b-1] , dist)
	arr[b-1][a-1] = min(arr[b-1][a-1], dist)

for k in range(n):
	for a in range(n):
		for b in range(n):
			arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])
			if a == b:
				arr[a][b] = 0
maxValue = 0
for i in range(n):
	tmp = 0
	for j in range(n):
		if arr[i][j] <= m:
			tmp += itemValueList[j]
	maxValue = max(tmp, maxValue)
print(maxValue)
