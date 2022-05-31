import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
sumForSub = 0
cnt = 1
result = [0] * n
tmp = 0

for i, v in enumerate(lst):
	sumForSub += result[tmp]
	result[i] = (cnt * v) - sumForSub
	tmp += 1
	cnt += 1

answer = []
answer.append(result[0])
for i in range(1, len(result)):
	answer.append(result[i] - result[i-1])
print(*answer)