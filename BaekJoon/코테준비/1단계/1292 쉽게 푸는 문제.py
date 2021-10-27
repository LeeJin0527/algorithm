import sys
input = sys.stdin.readline
answer = [[] for _ in range(46)]
new = []
a, b = map(int, input().split())
for i in range(1, 46):
	for j in range(i):
		answer[i].append(i)
# print(answer)
for i in answer:
	new += i
print(sum(new[a-1:b]))