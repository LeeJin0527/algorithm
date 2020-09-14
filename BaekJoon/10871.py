def answer(int):
    import sys
    #먼저 입력 두줄을 받아야 한다 .
    a,b=map(int,sys.stdin.readline().split())
    #a,b 입력 받음
    #a의 개수만큼 입력받으려면 리스트가 필요하다 이때는 맵핑한다.
    c=list(map(int,sys.stdin.readline().split()))
    #입력 완료
    #범위를 c로 잡으면 처음부터 비교 가능
    for i in c:
        if(b > i):
            print(i,end=' ')







if __name__ =='__main__':
    answer(int)