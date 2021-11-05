n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
search = list(map(int, input().split()))

def binary_search(array, target, start, end):
	while start <= end:
		mid = (start + end)// 2
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			end = mid -1
		else:
			start = mid + 1
	return None

for i in search:
	result = binary_search(lst, i, 0, n-1)
	if result == None:
		print('no', end = ' ')
	else:
		print('yes', end = ' ')

