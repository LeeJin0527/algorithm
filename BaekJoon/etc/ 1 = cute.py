import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
	lst.append(int(input()))
cute = lst.count(1)
ncute = lst.count(0)
if cute > ncute:
	print("Junhee is cute!")
else:
	print("Junhee is not cute!")