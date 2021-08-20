n, k = map (int, input().split())
count = 0

while True:
	if n % k == 0 :
		break
	n -= 1
	count += 1

while True:
	if n == 1:
		break
	n = n// k
	count += 1

print(count)