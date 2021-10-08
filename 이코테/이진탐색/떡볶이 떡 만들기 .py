n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def binary_search(array, target, start, end):

	mid = (start + end) // 2
	if start > end:
		return array[mid-1]
	cal = 0
	cal = sum([(i- array[mid]) for i in data if (i - array[mid]) >= 0])
	if cal == target:
		return array[mid]
	elif cal > target:
		return binary_search(array, target, mid +1, end)
	else:
		return binary_search(array, target, start, mid-1)

result = binary_search(data, m, 0, n-1)
print(result)