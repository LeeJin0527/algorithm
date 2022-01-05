import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
# for cycle : 값이 0인것들
isCycle = [False]*(n+1)
# not for cycle : BFS 돌리면서 값 증가할 것
isCheck = [False] * (n+1)
check = [-1] * (n+1)
# 사이클을 찾을 때 쓰임
def dfs(start, end, cnt):
	global cycle
	if cycle:
		return
	# 종료조건 : 시작점과 끝점이 같고 , 방문한 점이 2개 이상이다
	if start == end and cnt >= 2:
		cycle = True
		return
	# 현재지점 방문처리
	visited[end] = True
	# 현재노드와 연결된 노드 순회
	for i in graph[end]:
		# 역으로 돌아가지 않게 하기 위함 ex) 1-2-1
		if not visited[i]:
			dfs(start, i, cnt+1)
		# 종료조건에 닿으면 갯수 증가 시키지 않고 dfs
		if i == start and cnt >= 2:
			dfs(start, i, cnt)
	return
# 사이클이 아닌 노드의 값을 계산하기 위해 쓰임
def bfs():
	q = deque()
	# 사이클이면 값이 0이고 이것을 큐에 넣음 (방문처리 해야함)
	for i in range(1, n+1):
		if isCycle[i]:
			check[i] = 0
			q.append(i)
			isCheck[i] = True
	while q:
		x = q.popleft()
		# 관련 노드 순회
		for v in graph[x]:
			# 방문하지 않았으면 방문 처리후에  값을 1증가 시킨 후에 큐에 넣음
			if check[v] == -1:
				isCheck[v] = True
				check[v] = check[x] + 1
				q.append(v)
	# 답 출력
	for i in range(1, n+1):
		print(check[i], end = ' ')
# 양방향 간선 , 그래프 추가
for i in range(n):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
#노드를 순회할 때 마다 방문여부와 사이클 초기화
for i in range(1, n+1):
	visited = [False] * (n+1)
	cycle = False
	dfs(i, i, 0)
	# 해당 노드가 사이클이면 True
	if cycle:
		isCycle[i] = True
# 사이클이 아닌 노드의 값을 출력할 때  쓰임
bfs()