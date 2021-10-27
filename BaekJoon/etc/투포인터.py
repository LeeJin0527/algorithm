n = 5
m = 5
data = [1, 2, 3, 2, 5]
count = 0
interval_sum = 0
end = 0
for start in range(n):
	while interval_sum < m and end < n:
		interval_sum += data[end]
		end += 1
	if interval_sum == m:
		count += 1
	interval_sum -= data[start]
print(count)