# import itertools
# import operator as op
# from functools import reduce
#
# def nCr(n, r):
# 	if n < 1 or r < 0 or n < r:
# 		raise ValueError
# 	r = min(r, n-r)
# 	numerator = reduce(op.mul, range(n, n-r, -1), 1)
# 	denominator = reduce(op.mul, range(1, r+1), 1)
# 	return numerator // denominator
#
#
# n, m = map(int, input().split())
#
# data = list(input().split())
#
# data.sort()
#
# cnt = {}
# for i in data:
# 	try : cnt[i] += 1
# 	except: cnt[i] = 1
# # print(cnt)
#
# count = 0
# for x in itertools.combinations(data, 2):
# 	count += 1
#
# # print(count)
# sum = 0
# for i in cnt:
# 	if int(cnt[i]) > 1:
# 		# print(cnt[i])
# 		sum += (nCr((int(cnt[i])), 2))
#
# # print(sum)
#
# answer = count - sum
# print(answer)

n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
	array[x] += 1

result = 0

for i in range(1, m+1):
	n -= array[i]
	result += array[i] * n

print(result )