d = [0] * 30001
d[1] = 0
d[2] = 1
n = int(input())
for i in range(3, n+1):
	d[i] = d[i-1] + 1
	if d[i] % 2 == 0 :
		d[i] = min(d[i], d[i//2] + 1)
	if d[i] % 3 == 0:
		d[i] = min(d[i], d[i //3] +1)
	if d[i] % 5 == 0:
		d[i] = min(d[i], d[i//5] +1)
print(d[n])