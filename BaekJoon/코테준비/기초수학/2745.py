n, b = input().split()
result = 0

for i in range(len(n)):
	#0~9
	if 48 <= ord(n[i]) < 58:
		result += int(n[i]) * int(b) ** (len(n)-i-1)
	else:
		result += (ord(n[i])-55) * int(b) ** (len(n)-i-1)
print(result)

