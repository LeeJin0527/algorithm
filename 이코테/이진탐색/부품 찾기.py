import sys
def binary_search(array, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	if array[mid] == target:
		return mid
	elif array[start] > target:
		return binary_search(array, target, start, mid-1)
	else:
		return binary_search(array, target, mid+1, end)

n = int(input())
data = list(map(int, input().split()))
data.sort()
m = int(input())
compare = list(map(int, input().split()))

for i in compare:
	result = binary_search(data, i, 0, n-1)
	if result == None:
		print('no', end = ' ')
	else:
		print('yes', end =' ')