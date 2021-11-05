n = int(input())
lst = [0] * 1000001
for i in input().split():
	lst[int(i)] = 1
m = int(input())
check = list(map(int, input().split()))
for i in check:
	if lst[i] == 1:
		print('yes', end = ' ')
	else:
		print('no', end =' ')