n, m = map(int, input().split())
data = []
for i in range(n):
	data.append(list(map(int, input())))

cnt = 0
countEach = [0] * (m*n)
def dfs(x, y):
	global cnt
	if x < 0 or y < 0 or x >= n or y >=m:
		return False
	if data[x][y] == 0:
		countEach[cnt] += 1
		data[x][y] = 1

		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y-1)
		dfs(x, y+1)

		return True

	return False

count = 0

for i in range(n):
	for j in range(m):
		if dfs(i, j) == True:
			count += 1
			cnt += 1

print(count)


tmp = 0
for c in countEach:
	if tmp == count:
		break
	print(c, end =' ')
	tmp += 1
