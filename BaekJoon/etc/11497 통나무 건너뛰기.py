t = int(input())
for i in range(t):
	n = int(input())
	tmp = list(map(int, input().split()))
	tmp = sorted(tmp, reverse= True)
	# print(tmp)
	right = tmp[::2]
	left = [tmp[0]] +tmp[1::2]
	# print(right)
	# print(left)
	rr = []
	ll = []
	for i in range(1, len(right)):
		rr.append(right[i-1] - right[i])
	for i in range(1, len(left)):
		ll.append(left[i-1] - left[i])
	x = max(rr)
	y = max(ll)
	print(max(x, y))
