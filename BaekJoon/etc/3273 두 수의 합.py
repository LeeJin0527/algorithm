from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
x = int(input())
cnt = 0
for i in lst:
	if (x - i) in lst:
		cnt += 1
print(cnt //2)
