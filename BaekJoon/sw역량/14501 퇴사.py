'''
d[i] = max(d[i+1] , p[i] + d[i+t[i])
인덱스 넘어가면 이전날까지의 최대 수익
'''

import sys
input = sys.stdin.readline
n = int(input())
t = []
p = []
t = [0] + t
p = [0] + p
for i in range(n):
	a, b = map(int, input().split())
	t.append(a)
	p.append(b)

d = [0] * 21
for i in range(n, 0, -1):
	if (i + t[i]) > n+1:
		d[i] = d[i+1]
	else:
		d[i] = max(d[i+1], d[i+t[i]] + p[i])

print(d[1])