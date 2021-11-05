import heapq
from collections import deque
import sys
input = sys.stdin.readline
def find_parent(parent, x):
	if x != parent[x]:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
edges = []
result = 0
parent = [0] * ( v+1)
for i in range(1,v+1):
	parent[i]  = i
for i in range(e):
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))
edges.sort()
last = 0
for e in edges:
	cost, a, b = e
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost
		last = cost
print(result - last)


