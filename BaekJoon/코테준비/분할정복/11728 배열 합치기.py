import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lstA = list(map(int, input().split()))
lstB = list(map(int, input().split()))
answer = lstA + lstB
answer.sort()
for i in answer:
	print(i, end = ' ')