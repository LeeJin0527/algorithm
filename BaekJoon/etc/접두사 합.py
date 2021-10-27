n = 5
data = [10, 20, 30, 40, 50]
sum_value = 0
prefix_sum = [0]
for i in data:
	sum_value += i
	prefix_sum.append(sum_value)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left -1])