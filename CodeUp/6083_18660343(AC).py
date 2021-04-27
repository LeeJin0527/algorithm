
answer = input().split(" ")
cnt =0
for i in range(int(answer[0])):
    for j in range(int(answer[1])):
        for k in range(int(answer[2])):
            print(i, j, k)
            cnt += 1
print(cnt)
