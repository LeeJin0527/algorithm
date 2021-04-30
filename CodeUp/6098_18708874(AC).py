

if __name__ == "__main__":
    x = 1
    y = 1
    tmp =[list(map(int, input().split())) for _ in range(10)]
    while(1):
            if tmp[y][x] == 2:
                tmp[y][x] = 9
                break
                # 시작점에 0이 있다
                #1이 나올때 까지 오른쪽으로 이동
            if tmp[y][x] == 0:
                tmp[y][x] = 9
                if tmp[y][x+1] != 1:
                    tmp[y][x] = tmp[y][x+1]
                    tmp[y][x] = 9
                    x = x+1
                    #print("2341234124")
                # 옆에 있는게 1 일때
                #아래로 내려감
                else:
                    #print("asdfadsfadsf")
                    if tmp[y+1][x] != 1:
                        tmp[y][x] = tmp[y+1][x]
                        tmp[y][x] = 9
                        y = y+1
                    else:
                        break

    for y in range(10):
        for x in range(10):
            print(tmp[y][x],end=' ' )
        print()







