import sys
import heapq
input = sys.stdin.readline
t = int(input())
for i in range(t):
	lst = []
	n = int(sys.stdin.readline().rstrip())
	if n // 11 == 0:
		answer = []
		lst = list(map(int, input().split()))
		left = []
		right = []
		for i, v in enumerate(lst):
			if len(left) == len(right):
				heapq.heappush(left, -v)
			else:
				heapq.heappush(right, v)
			if right and -left[0] > right[0]:
				lf = heapq.heappop(left)
				rg = heapq.heappop(right)
				heapq.heappush(left, -rg)
				heapq.heappush(right, -lf)
			if i % 2 == 0:
				answer.append(-left[0])
		print(n // 2 + 1)
		print(*answer)
	else:
		answer = []
		lst = [list(map(int, input().split())) for j in range(n//10+1)]
		# print(lst)
		left = []
		right = []
		row = n // 10
		for i in range(row+1):
			if i == row:
				for j in range(n % 10):
					if len(left) == len(right):
						heapq.heappush(left, -lst[i][j])
					else:
						heapq.heappush(right, lst[i][j])
					if right and -left[0] > right[0]:
						lf = heapq.heappop(left)
						rg = heapq.heappop(right)
						heapq.heappush(left, -rg)
						heapq.heappush(right, -lf)
					if j % 2 == 0:
						answer.append(-left[0])
			else:
				for j in range(10):
					if len(left) == len(right):
						heapq.heappush(left, -lst[i][j])
					else:
						heapq.heappush(right, lst[i][j])
					if right and -left[0] > right[0]:
						lf = heapq.heappop(left)
						rg = heapq.heappop(right)
						heapq.heappush(left, -rg)
						heapq.heappush(right, -lf)

					if j % 2 ==0:
						answer.append(-left[0])

		print(n // 2 + 1)
		for i in range(0, len(answer), 10):
			print(*answer[i:i+10])

