# Algorithm
매일 매일 1문제 이상 풀자 아자아자아자

## 2021-04-22 ~
## ~ 2021-05-01 
numpy update하기
## 1. 다양한 입력

### 1-1. 나누어 입력 받기 
        1 2
        a, b = map(int, input().split())
        
        
        
### 1-2. 입력 출력 가속
        from sys import stdin
        input = sys.stdin.readline
        print = sys.stdout.write
        
        

## 2. 배열 입력


### 2-1. 배열 입력
        3
        1 2 3
        4 5 6
        7 8 9
        
        MAP = [list(map(int, input().split())) for _ in range(int(input())))]
        
        
        
### 2-2. 정수와 배열이 같은 줄에 들어오는 경우 
        4 10 20 30 40 
        3 7 5 12
        3 125 15 25
        
        N, *arr = map(int, input().split())
        
### 2-3. 문자열을 한 글자씩 배열에 저장
        3
        AAAA
        ABCA
        AAAA
        
        arr = [['A', 'A', 'A', 'A']
               ['A', 'B', 'C', 'A']
               ['A', 'A', 'A', 'A']]
               
        arr =[list (input()) for _ in range(N)]
        
 ## 3.배열 출력
 
 ### 3-1 .배열을 연결해서 출력
        arr =[1, 2, 3, 4]
        1234
        
        arr =[1, 2, 3, 4]
       1번째 방법
       
       print("".join(map(str,arr))
       
       2번째 방법 
       
       print(*arr)
       
       
       
## 보너스 
          3
          1 2 3
          4 5 6
          7 8 9
          
          위와 다르게 
          끝을 알 수 없는 입력이 들어온다면?
        
        
          try :
              while 1:
                  a, b = map(int, input().split())
                  print(a + b)
          except:
               exit()
                  
                  
                  
  reference :https://covenant.tistory.com/141
  # 인덱스 찾기 
  target = array.index(min(tmp)) 
  
  # 더 빠른 입력

    import sys
    input_data = sys.stdin.readline().rstrip()
    print(input_data)
    
    import sys
    input = sys.stdin.readline
    INF = int(1e9)

 # 누적합 
           for i, v in enumerate(list):
                sum += v
                accu += sum
           print(accu)
