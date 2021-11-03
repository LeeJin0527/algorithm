def binary_search(array, target, start, end):
	while start <= end:
		mid = (start + end) // 2
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			end = mid -1
		else:
			start = mid + 1
	return None
n, target = map(int, input().split())
lst = list(map(int, input().split()))
result = binary_search(lst, target, 0, n-1)
if result == None:
	print('찾는 원소가 없음 ')
else:
	print(result + 1)