import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
	end, ant = map(int, input().split())
	lst = []
	for i in range(ant):
		lst.append(int(input()))
	maxTime = 0
	minTime = 0
	lst.sort()
	for i in lst:
		minTime = max(minTime, min(i, end-i))
		maxTime = max(maxTime, i, end-i)
	print(minTime, maxTime)