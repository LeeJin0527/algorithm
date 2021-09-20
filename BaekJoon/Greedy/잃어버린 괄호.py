n = input()
n = n.split('-')
# print(n)


for i, v in enumerate(n):
	tmp = 0
	# print(i)

	if '+' in v:
		v = v.split('+')
		for j in v:
			tmp += int(j)

		if i == 0:
			sum = tmp
		else:
			sum -= tmp
	else:
		if i == 0:
			sum = int(v)
		else:
			sum -= int(v)


print(sum)