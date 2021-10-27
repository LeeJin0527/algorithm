
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)
answer = list(permutations(data, 2))
print(answer)

x = list(product(data, repeat= 2))
print(x)

y = list(combinations_with_replacement(data, 2))
print(y)

lam = sorted(
	[('홍길동', 30),('아무게', 50), ('이순신', 10)], key = lambda x: x[1], reverse= True
)
print(lam)