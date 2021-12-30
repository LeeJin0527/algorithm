import sys

n = sys.stdin.readline().rstrip()
lst = list(n)
lst = list(map(int, lst))
lst.sort(reverse=True)
lst = list(map(str, lst))
lst = ''.join(lst)
print(lst)