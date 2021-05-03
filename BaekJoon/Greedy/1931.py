N = int(input())
tmp =[]
# = [list(map(int(input().split() for _ in range(N))))]

for i in range(N):
	t1 , t2 = input().split()
	tmp.append([int(t1), int(t2)])

tmp.sort(key = lambda x: (x[1], x[0]))


cnt =1
j = 0
for i in range(1, N):


	if tmp[i][0] >= tmp[j][1]:

		j = i-1
		#print( print(tmp[j][1]) ,cnt)
		cnt += 1

	else:
		j = j -1

	j = j+1

print(cnt)












