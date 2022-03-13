coins = [10, 50, 100, 500]
coins.sort(reverse = True)
n = 1260
cnt = 0
for i in coins:
	cnt += n // i
	n = n % i
print(cnt)