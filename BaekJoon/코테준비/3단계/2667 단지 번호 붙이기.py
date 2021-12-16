#dfs
n = int(input())
lst = []
for i in range(n):
	lst.append(list(map(int, input())))


def dfs(x, y):
	global valid
	if x < 0 or y < 0 or x >= n or y >=n:
		return False
	if lst[x][y] == 1:
		lst[x][y] = 0
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y-1)
		dfs(x, y+1)
		valid += 1
		return True
	return False


cnt = 0
visited = []
for i in range(n):
	for j in range(n):
		valid = 0
		if dfs(i, j) == True:
			cnt += 1
			visited.append(valid)
visited.sort()

print(cnt)
for i in visited:
	print(i)

