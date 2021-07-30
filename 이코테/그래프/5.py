# 특정 원소가 속합 집합을 찾기
def find_parent(parent, x):
	# 루트 노드가 아니라면 루트 노드를 찾을 때 까지 재귀적으로 호출
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

#  두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a <  b:
		parent[b] = a
	else:
		parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 상에서 , 부모를 자기 자신으로 초기화
for i in range(1, v+1):
	parent[i] =i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))

edges.sort()

for edge in edges:
	cost, a, b = edge
	if find_parent(parent,a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost

print(result)