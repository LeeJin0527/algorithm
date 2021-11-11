n, m = map(int, input().split())
answer = []
for i in range(1, n+1):
	if n % i == 0:
		answer.append(i)
tmp = m-1
if tmp >= len(answer):
	answer = 0
	print(0)
	exit()
print(answer[tmp])

