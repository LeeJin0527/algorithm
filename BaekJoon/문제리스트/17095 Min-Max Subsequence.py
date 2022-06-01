import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
Min, Max = min(lst), max(lst)
ans, minIndex, maxIndex = n+1, -1, -1
for i, v in enumerate(lst):
	if v == Min:
		minIndex = i
		if maxIndex != -1:
			ans = min(ans, abs(maxIndex - minIndex))
	if v == Max:
		maxIndex = i
		if minIndex != -1:
			ans = min(ans, abs(maxIndex - minIndex))
print(ans+1)