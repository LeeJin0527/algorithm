import sys
import copy
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
graph = []
safety = set()
for i in range(n):
	graph.append(list(map(int, input().split())))
	for j in range(len(graph[i])):
		safety.add(graph[i][j])

def dfs(tmp, x, y, k):
	if x < 0 or y < 0 or x >= n or y >= n:
		return False
	if tmp[x][y] >= k:
		tmp[x][y] = 0
		dfs(tmp, x-1, y, k)
		dfs(tmp, x+1, y, k)
		dfs(tmp, x, y-1, k)
		dfs(tmp, x, y+1, k)
		return True
	return False

answer = 0
for k in safety:
	tmp = copy.deepcopy(graph)
	cnt = 0
	for i in range(n):
		for j in range(n):
			if dfs(tmp, i, j, k):
				cnt += 1
	answer = max(answer, cnt)
print(answer)