import sys
n, m = map(int, input().split())
x = int(input())
tmp = n * 60 + m + x

hour = (tmp // 60) % 24
minute = (tmp % 60) % 60
print(hour, minute)