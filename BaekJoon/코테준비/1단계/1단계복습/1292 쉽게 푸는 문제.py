n, m = map(int, input().split())
answer = []
for i in range(1, 46):
	for j in range(i):
		answer.append(i)
new = answer[n-1: m]
print(sum(new))