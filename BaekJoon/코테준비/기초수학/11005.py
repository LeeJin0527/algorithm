n, b = map(int, input().split())
answer = []
while True:
	if n <= 1:
		break
	answer.append(n % b)
	n = n // b
answer.reverse()

if n != 0:
	result = str(n)
	for i in answer:
		if i >= 10:
			result += str(chr(i+55))
		else:
			result += str(i)
	print(result)
else:
	result = ''
	for i in answer:
		if i >= 10:
			result += str(chr(i+55))
		else:
			result += str(i)
	print(result)