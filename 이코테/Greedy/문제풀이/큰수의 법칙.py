n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

first = data[0]
second = data[1]

share = m //(k+1)
remainder = m % (k+1)

answer = share * (first * k + second) + first * remainder
print(answer)