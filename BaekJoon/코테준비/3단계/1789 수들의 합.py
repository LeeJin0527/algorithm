s = int(input())
result = 0
cnt = 0
i = 1
while True:
	if result == s:
		break
	elif result > s:
		cnt -= 1
		break
	result += i
	i += 1
	cnt += 1
print(cnt) 
