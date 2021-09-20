n = int(input())
left = 1000 - n
coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coins:
	cnt += left // coin
	left = left % coin
print(cnt)
