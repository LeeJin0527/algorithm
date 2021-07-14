# 메모리의 한 곳을 동시에 가리킴
dp = [[]] * 10
dp[0].append(1)
print(dp)
# 메모리의 각각의 곳을 가리킴
dp = [[] for _ in range(10)]
dp[0] = 0
print(dp)

# 동시에 가리키고 개별적으로 변경
dp = [1]*10
dp[0] = 0
print(dp)
# 동시에 가리키고 개별적으로 변경
dp = [None] * 10
dp[0] = 0
print(dp)