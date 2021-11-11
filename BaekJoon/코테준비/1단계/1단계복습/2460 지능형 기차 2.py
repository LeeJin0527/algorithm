answer = 0
for i in range(10):
	x, y = map(int, input().split())
	if i == 0:
		start = y
	else:
		start += y-x
		answer = max(answer, start)
print(answer)