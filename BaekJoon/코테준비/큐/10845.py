from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for i in range(n):
	lst = input().split()
	if lst[0] == 'push':
		q.append(int(lst[1]))
	elif lst[0] == 'pop':
		try:
			x = q.popleft()
			print(x)
		except:
			print(-1)
	elif lst[0] == 'size':
		print(len(q))
	elif lst[0] == 'empty':
		if len(q) == 0:
			print(1)
		else:
			print(0)
	elif lst[0] == 'front':
		try:
			print(q[0])
		except:
			print(-1)
	elif lst[0] == 'back':
		try:
			print(q[-1])
		except:
			print(-1)
