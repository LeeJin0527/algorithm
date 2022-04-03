# 1번 풀이 
import sys
import math
input = sys.stdin.readline
h, w, n, m = map(int, input().split())
print(math.ceil(h / (n+1)) * math.ceil(w / (m+1)))


# 2번 풀이 
import sys
input = sys.stdin.readline
h, w, n, m = map(int, input().split())
row = 0
col = 0
if h % (n+1) == 0:
	row = h // (n+1)
else:
	row = (h // (n+1) )+ 1
if w % (m+1) == 0:
	col = w // (m+1)
else:
	col = (w // (m+1)) + 1
print(row * col)
