s = int(input())
sum = 0
cnt = 0
i = 0
while True:
	i = i+1
	sum += i
	cnt += 1
	if sum > s:
		cnt -= 1
		break
print(cnt)

