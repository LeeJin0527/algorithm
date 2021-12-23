n, m = map(int, input().split())
graph = []
for i in range(m):
	graph.append(list(input()))
def Wdfs(x, y):
	global Weach
	if x < 0 or y < 0 or x >= m or y >= n:
		return False
	if graph[x][y] == 'W':
		graph[x][y] = 0
		Wdfs(x-1, y)
		Wdfs(x+1, y)
		Wdfs(x, y-1)
		Wdfs(x, y+1)
		Weach += 1
		return True
	return False

def Bdfs(x, y):
	global Beach
	if x < 0 or y < 0 or x >= m or y >= n:
		return False
	if graph[x][y] == 'B':
		graph[x][y] = 1
		Bdfs(x-1, y)
		Bdfs(x+1, y)
		Bdfs(x, y-1)
		Bdfs(x, y+1)
		Beach += 1
		return True
	return False
WList = []
BList = []
cnt = 0

for i in range(n):
	for j in range(m):
		Weach = 0
		Beach = 0
		if Wdfs(j, i) == True:
			WList.append(Weach)
		if Bdfs(j, i) == True:
			BList.append(Beach)
WSum = 0
BSum = 0

for i in WList:
	WSum += i**2
for i in BList:
	BSum += i**2
print(WSum, BSum)
