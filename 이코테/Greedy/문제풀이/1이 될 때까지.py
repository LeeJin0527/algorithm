n, k = map(int, input().split())

cnt = 0

while True:
	if n % k == 0:
		break
	n -= 1
	cnt += 1


while True:
	if n == 1:
		break
	n = n // k
	cnt += 1

print(cnt)
