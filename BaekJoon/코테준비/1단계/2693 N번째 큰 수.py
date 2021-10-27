t = int(input())
for i in range(t):
	answer = list(map(int, input().split()))
	answer = sorted(answer)
	print(answer[-3])