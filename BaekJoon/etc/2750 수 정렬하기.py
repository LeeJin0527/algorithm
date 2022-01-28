n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
for i in range(n):
    print(lst[i])
