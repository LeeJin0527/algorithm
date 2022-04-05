import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
cnt = 0
for i in range(n):
	tmp = lst[:i] + lst[i+1:]
	left, right = 0, len(tmp)-1
	while left < right:
		t = tmp[left] + tmp[right]
		if lst[i] == t:
			cnt += 1
			break
		if lst[i] < t:
			right -= 1
		else:
			left += 1
print(cnt)