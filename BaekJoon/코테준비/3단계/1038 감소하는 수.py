import sys
from itertools import combinations
n = int(sys.stdin.readline())
answer = []
for i in range(1, 11):
	for j in combinations(range(0, 10) ,i):
		j = list(j)
		j.sort(reverse= True)
		answer.append(int("".join(map(str, j))))
answer.sort()
try:
	print(answer[n])
except:
	print(-1)


