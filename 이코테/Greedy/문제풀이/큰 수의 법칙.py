n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

first = data[0]
second = data[1]

result = (k * first + second) * (m // (k+1))

result += first * (m % (k+1))

print(result)

