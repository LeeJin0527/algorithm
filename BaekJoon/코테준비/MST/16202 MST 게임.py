import copy
v, e, turn = map(int, input().split())
def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_find(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

edges = []
compare = set()
for i in range(e):
	a, b = map(int, input().split())
	cost = i+1
	edges.append((cost, a, b))
	compare.add(a)
	compare.add(b)
edges.sort()
# 한 집합 안에 있는지 확인
compareList = [min(compare)] * v
compareList = [0] + compareList

tmpEdges = copy.deepcopy(edges)
for i in range(turn):
	result = 0
	tmpEdges = edges[i:]
	parent = [0] * (v+1)
	for j in range(1, v+1):
		parent[j] = j
	for edge in tmpEdges:
		cost, a, b = edge
		if find_parent(parent, a) != find_parent(parent, b):
			union_find(parent, a, b)
			result += cost
	for i in range(1, v+1):
		find_parent(parent, i)

	if parent != compareList:
		print(0, end = ' ')
	if parent == compareList:
		print(result, end = ' ')