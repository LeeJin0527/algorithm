import sys
input = sys.stdin.readline
n = int(input())
answer = []
for i in range(n):
	answer.append(int(input()))
answer.sort()
for i in answer:
	print(i)