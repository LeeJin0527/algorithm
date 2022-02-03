import sys
from itertools import combinations
import math

input = sys.stdin.readline
n = int(input())
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

parent = [0] * (n+1)
edges = []
result = 0
star = []
for i in range(n):
	star.append(list(map(float, input().split())))

for i in range(1, n+1):
	parent[i] = i

lst = [i for i in range(n)]
for i in list(combinations(lst, 2)):
	a, b = i[0], i[1]
	tmp = round(math.sqrt((star[a][0]-star[b][0]) **2 + (star[a][1]-star[b][1])**2), 2)
	edges.append((tmp, a, b))
edges.sort()

for edge in edges:
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_find(parent, a, b)
		result += cost
print(result)