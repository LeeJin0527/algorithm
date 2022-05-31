import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
maxValue = max(lst)
minValue = min(lst)
print(maxValue - minValue)