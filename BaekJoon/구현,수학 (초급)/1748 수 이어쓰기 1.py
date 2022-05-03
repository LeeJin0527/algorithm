import sys
n = int(input())
lst = ['9' + '0' *(i) for i in range(len(str(n)))]
result = 0
for i, v in enumerate(lst):
	if v == lst[-1]:
		result += len(v) * (n - 10 ** (len(str(n))-1) +1)
	else:
		result += (i+1) * int(v)
print(result)
