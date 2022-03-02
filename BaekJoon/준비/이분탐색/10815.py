import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
compare = list(map(int, input().split()))
def bin_search(arr, target, start, end):
	while start <= end:
		mid = (start+end) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			end = mid-1
		else:
			start = mid +1
	return None

for i in compare:
	result = bin_search(lst, i, 0, n-1)
	if result == None:
		print(0, end = ' ')
	else:
		print(1, end = ' ')
