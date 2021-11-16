import math
n = int(input())
answer = []

while True:

	start = n
	n = math.ceil(n / (-2))
	answer.append(start - n*(-2))
	if n == 0:
		break
answer.reverse()
for i in answer:
	print(i, end = '')

