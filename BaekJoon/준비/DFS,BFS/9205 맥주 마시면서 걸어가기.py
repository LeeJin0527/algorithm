import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	n = int(input())
	cur_x, cur_y = map(int, input().split())
	lst = []
	visited = []
	check = False
	for i in range(n):
		x, y = map(int, input().split())
		lst.append([x, y])
	end_x, end_y = map(int, input().split())
	lst.append([end_x, end_y])
	q = deque()
	q.append([cur_x, cur_y])
	while q:
		x, y = q.popleft()
		if x == end_x and y == end_y:
			check = True
			break
		for k in lst:
			if abs(k[0] - x) + abs(k[1] - y) <= 1000 and [k[0], k[1]] not in visited:
				visited.append([k[0], k[1]])
				q.append([k[0], k[1]])
	if check:
		print('happy')
	else:
		print('sad')