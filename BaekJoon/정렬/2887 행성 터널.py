import sys
import copy
input = sys.stdin.readline

def find_parent(parent, x):
	if parent[x] != x :
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_find(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b
n = int(input())
planet = []
for i in range(n):
	planet.append( tuple(map(int, input().split())) +(i, ) )


x = copy.deepcopy(planet)
y = copy.deepcopy(planet)
z = copy.deepcopy(planet)
x.sort(key=lambda x : x[0])
y.sort(key=lambda x : x[1])
z.sort(key=lambda x : x[2])

edges = []
for i in range(len(x)-1):
	edge = (abs(x[i+1][0] -x[i][0]), x[i][-1], x[i+1][-1])
	edges.append(edge)
for i in range(len(y)-1):
	edge = (abs(y[i+1][1] -y[i][1]), y[i][-1], y[i+1][-1])
	edges.append(edge)
for i in range(len(z)-1):
	edge = (abs(z[i+1][2] -z[i][2]), z[i][-1], z[i+1][-1])
	edges.append(edge)
edges.sort()
print(edges)
parent = [0] * (n)
for i in range(n):
	parent[i] = i
result = 0
for e in edges:
	distance, a, b = e
	if find_parent(parent, a) != find_parent(parent, b):
		union_find(parent, a, b)
		result += distance
print(result)
