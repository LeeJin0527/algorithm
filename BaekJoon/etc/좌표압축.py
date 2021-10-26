import sys
input = sys.stdin.readline

n = int(input())
tmp = list(map(int, input().split()))
new = list(set(tmp))
new = sorted(new)
# print(new)
answer = dict()
for i, v in enumerate(new):
	answer[v] = i
# print(answer)

for i in tmp:
	print(answer[i], end = ' ')