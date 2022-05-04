import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m, k = map(int, input().split())
lst = [[0] * m for _ in range(n)]


for _ in range(k):
	x1, y1, x2, y2, = map(int, input().split())
	x2 -= 1
	y2 -= 1

	for i in range(x1, x2 + 1):
		for j in range(y1, y2 + 1):

			lst[j][i] = 1

def dfs(x, y):
	global cnt
	if x < 0 or y < 0 or x >= n or y >= m:
		return False
	if lst[x][y] == 0:
		lst[x][y] = 1
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y+1)
		dfs(x, y-1)
		cnt += 1
		return True
	return False

result = []


for i in range(n):
	for j in range(m):
		cnt = 0
		if dfs(i, j):
			result.append(cnt)
result.sort()
print(len(result))
print(*result)
