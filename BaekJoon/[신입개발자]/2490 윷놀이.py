from collections import defaultdict, Counter
A = Counter([0, 1, 1, 1])
B = Counter([0, 0, 1, 1])
C = Counter([0, 0, 0, 1])
D = Counter([0, 0, 0, 0])
E = Counter([1, 1, 1, 1])


for _ in range(3):
	x = Counter(list(map(int, input().split())))
	if x == A:
		print('A')
	elif x == B:
		print('B')
	elif x == C:
		print('C')
	elif x == D:
		print('D')
	else:
		print('E')

