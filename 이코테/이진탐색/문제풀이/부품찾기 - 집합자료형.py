n = int(input())
array = set(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

for i in target:
	if i in array:
		print('yes', end = ' ')
	else:
		print('no' , end = ' ')