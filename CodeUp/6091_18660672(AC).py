
answer = input().split(" ")
d = 1
while d % int(answer[0]) != 0 or d % int(answer[1]) != 0 or d % int(answer[2]) != 0:
    d += 1
print(d)
