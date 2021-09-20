t = int(input())
lines = [300, 60, 10]
answer = [0, 0, 0]


for i, line in enumerate(lines):
	if t // line >= 1:
		answer[i] = t // line

	t = t % line


if t != 0:
	print('-1')
else:

	for i in answer:
		print(i, end = ' ')