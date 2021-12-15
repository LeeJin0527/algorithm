import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for i in range(n):
	lst.append(int(input()))
# print(lst)
'''
  1 2 3 4 5 6 7 8 9 10 
1 1 1 1 1 1 1 1 1 1 1
2 0 1 1 2 2 3 3 4 4 5
5 0 0 0 0 1 1 2 2 3 4
s 1 2 2 3 4 5 6 7 8 10

d[i] = d [j-i]
'''
d = [0] * (k+1)
d[0] = 1
for i in lst:
	for j in range(i, k+1):
		if j >= i:
			d[j] += d[j-i]
print(d[k])


