N, M, K = map(int, input().split( ))
tmp = list(map(int, input().split()))
answer = 0
cnt = 0
tmp.sort()
#print(tmp)
if tmp.count(max(tmp)) >=2 :
	answer = M * max(tmp)
else:
	while(True):
		answer += K * tmp[-1]
		cnt += K
		answer += tmp[-2]
		cnt +=1

		if cnt ==M :
			break

print(answer)

#%% 모범 답안
# n, m, k =map(int, input().split())
# data =list(map(int, input().split()))
# 
# data.sort()
# first = data[n-1]
# second = data[n-2]
# 
# count = int(m/ (k+1)) * k
# count += m % (k+1)
# 
# result = 0
# result += (count) *first
# result += (m -count) *second
# 
# print(result)
