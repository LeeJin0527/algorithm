def fac(x):
	if x == 0:
		return 1

	return x* fac(x-1)
x = int(input())
lst = list(str(fac(x)))
lst.reverse()
cnt = 0
i = 0
while True:
	if lst[i] != '0' and i <= len(lst):
		break
	cnt += 1
	i += 1
print(cnt)

