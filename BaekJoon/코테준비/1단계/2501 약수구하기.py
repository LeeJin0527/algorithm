n, k = map(int, input().split())
answer = [0 for _ in range(10001)]
j = 0
for i in range(1, n+1):
	if n % i == 0:
		answer[j] = i
		j += 1
print(answer[k-1])

