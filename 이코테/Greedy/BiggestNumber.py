N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
x = M //(K+1)
y = M % (K +1)
first = data[0]
second = data[1]
sum1 = (first * K + second) * x
sum2 = (first * y)
print(sum1 + sum2)
