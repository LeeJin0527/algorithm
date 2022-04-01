import sys
origin = sys.stdin.readline().rstrip()
compare = sys.stdin.readline().rstrip()
a = origin.count('a')
c = compare.count('a')
if ( a >= c):print('go')
else: print('no')