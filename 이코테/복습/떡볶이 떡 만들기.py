n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = 0
def binary_search(array, target, start, end):
	while start <= end:
		total = 0
		mid = (start + end) // 2
		for i in array:
			if i > array[mid]:
				total += (i - array[mid])
		if total < target:
			end = mid - 1
		else:
			result = mid
			start = mid + 1
	return result
result = binary_search(lst, m, 0, n-1)
print(lst[result])