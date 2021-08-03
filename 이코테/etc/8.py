from itertools import permutations
from itertools import combinations
from itertools import product
data = ['A','B', 'C']
result = list(permutations(data, 3))
print(result)

result = list(combinations(data, 2))
print(result)

result = list(product(data, repeat=2))
print(result)