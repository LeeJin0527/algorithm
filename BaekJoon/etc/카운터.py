from collections import Counter

counter = Counter(['red', 'yellow', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))