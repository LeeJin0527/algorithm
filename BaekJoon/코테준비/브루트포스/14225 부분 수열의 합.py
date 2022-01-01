import sys
from itertools import combinations
input = sys.stdin.readline
s = int(input())
lst = list(map(int, input().split()))
lst.sort()
'''
1 2 5
1 12 125
'''
answer = []
k = 1
answer = []
for i in range(1, s+1):
	for j in list(combinations(lst, i)):
		answer.append(sum(j))

k = 1
answer = set(answer)
for i in answer:
	if k not in answer:
		print(k)
		exit()
	k+=1
print(k) 
