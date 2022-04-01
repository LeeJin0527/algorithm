import sys
input = sys.stdin.readline().rstrip()
n = int(input)
for _ in range(n):
	loc, arr = sys.stdin.readline().rstrip().split()
	arr = list(arr)
	del arr[int(loc)-1]
	print(''.join(arr))