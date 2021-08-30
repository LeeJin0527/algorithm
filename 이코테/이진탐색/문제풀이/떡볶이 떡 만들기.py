n, m = map(int, input().split())
total = list(map(int, input().split()))
total.sort()
# print(total)

def binary_search(array, start, end):
	global Sum
	global tmp

	# print(start, end )
	mid = (start + end) // 2
	if start > end: return

	# print('mid', mid)

	Sum = 0
	for i in total:
		tmp = i - mid
		if tmp > 0:
			Sum += tmp

	# print('Sum: m',Sum, m)

	if Sum < m:
		# print('big', Sum)
		return binary_search(array, start, mid -1)
	elif Sum == m:
		tmp = mid
		return tmp

	else:
		tmp = mid
		return binary_search(array, tmp + 1, end)

Sum = 0
tmp = 0
result = binary_search(total, total[0], total[-1])

print(tmp)

