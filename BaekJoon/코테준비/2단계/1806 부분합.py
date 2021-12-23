n, s = map(int, input().split())
lst = list(map(int, input().split()))
count = 0
interval_sum = 0
answer = 1e9
end = 0
for start in range(n):
	while interval_sum < s and end < n:
		interval_sum += lst[end]
		end += 1
	if interval_sum >= s:
		answer = min(answer, end - start)
	interval_sum -= lst[start]
if answer == 1e9:
	print(0)
else:
	print(answer)
 
