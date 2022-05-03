import sys
input = sys.stdin.readline
n = int(input())
for i in range(1, n+1):
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	resultA = 0
	resultA += a[0] * 1
	resultA += a[1] * 2
	resultA += a[2] * 3
	resultA += a[3] * 3
	resultA += a[4] * 4
	resultA += a[5] * 10
	resultB = 0
	resultB += b[0] * 1
	resultB += b[1] * 2
	resultB += b[2] * 2
	resultB += b[3] * 2
	resultB += b[4] * 3
	resultB += b[5] * 5
	resultB += b[6] * 10


	if resultA < resultB:
		print("Battle" , str(i) +":", "Evil eradicates all trace of Good" )
	elif resultA > resultB:
		print("Battle" , str(i) +":", "Good triumphs over Evil" )
	else:
		print("Battle" , str(i) +":", "No victor on this battle field" )