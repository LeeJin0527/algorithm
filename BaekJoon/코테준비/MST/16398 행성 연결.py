import sys
input = sys.stdin.readline

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
lst = []

v = int(input())
for i in range(v):
	lst.append(list(map(int, input().split())))
parent = [0] * (v)
edges = []
result = 0
for i in range(v):
	parent[i] = i
for i in range(v):
	for j in range(v):
		if i == j:
			break
		else:
			edges.append((lst[i][j], i, j))

edges.sort()

for edge in edges:
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_find(parent, a, b)
		result += cost
print(result)
