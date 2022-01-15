from itertools import permutations
import sys
input= sys.stdin.readline
n, d = map(int, input().split())

left = []
while True:
	left.append(n % d)
	n = n // d
	if n == 0:
		break
left.reverse()
left = list(map(str, left))
left = int(''.join(left))

#  비교
compare = [i for i in range(d)]
compare.reverse()
INF = int(1e9)+1
result = INF
def dfs(num, cnt):
	global result
	if num > left:
		lenMin = [int(a) for a in str(num)]
		if len(lenMin) == len(compare):
			result = min(result, num)
	# 방문 후 백트래킹
	for i in compare:
		if isValid(10*num + i, cnt+1):
			dfs(10*num+i, cnt+1)
	return result

def isValid(x, tmp):
	# 0~ d까지 한번씩만 나와야한
	x = set([int(a) for a in str(x)])
	if len(x) == tmp:
		return True
	return False


for num in compare:
	dfs(num, 1)
if result == INF:
	print(-1)
	exit()

result = [int(a) for a in str(result)]
result.reverse()
answer = 0
for i, v in enumerate(result):
	answer += v * (d**i)
print(answer)