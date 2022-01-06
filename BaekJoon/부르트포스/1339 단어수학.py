import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
	graph.append(list(sys.stdin.readline().rstrip()))
arrList = [0] * 27
for i in graph:
	for j in range(len(i)):
		# print(ord(i[j])-65, len(i)-j-1)
		arrList[ord(i[j])-65] += 10 ** (len(i)-j-1)
arrList.sort(reverse=True)
answer = 0
for i in range(9, -1, -1):
	answer += arrList[9-i] * i
print(answer)