n = int(input())
graph = []
for i in range(n):
	graph.append(list(map(int, input())))
# print(graph)
each = 0
def dfs(x, y):
	global each
	if x < 0 or y < 0 or y >= n or x >= n:
		return False
	if graph[x][y] == 1:
		graph[x][y] = 0
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y-1)
		dfs(x, y+1)
		each += 1
		return True
	return False

cnt = 0

answer = []
for i in range(n):
	for j in range(n):
		each = 0
		if dfs(i, j) == True:
			cnt += 1
			answer.append(each)


print(cnt)
answer = sorted(answer)
for i in answer:
	print(i)
# print(answer)
