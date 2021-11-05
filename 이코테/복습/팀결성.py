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
parent = [0] * (v+1)

for i in range(1, v+1):
	parent[i] = i

for i in range(e):
	a, b, c = map(int, input().split())
	if a == 0:
		union_parent(parent, b, c)
	elif a == 1:
		if find_parent(parent, b) != find_parent(parent, c):
			print('NO')
		else:
			print('YES')