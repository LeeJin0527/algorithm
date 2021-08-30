n = int(input())
total = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

total.sort()
target.sort()

def binary_search(array, target, start, end):

	mid = (start + end) // 2
	if start > end:
		return None
	if array[mid] == target :
		return mid
	elif array[mid] > target:
		return binary_search(array, target, start, mid -1)
	else:
		return binary_search(array, target, mid+1, end)

for i in target:
	target = i
	result = binary_search(total, target, 0, n-1)

	if result == None:
		print('no', end = ' ')
	else:
		print('yes', end =' ')