# Algorithm
매일 매일 1문제 이상 풀자 아자아자아자
## 2022 -02-02 ~ 프로그래머스 시작


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
           
# sort 조건
           line = sorted(line, key = lambda x : (x[1], x[0]) )
           #1순위, 2순위 
           
# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

       1부터 더해서 sum 이 s 보다 커지면 그에 맞는 수를 하나 빼는 방식으로 n 값을 구할 수 있다 
# 리스트 초기화 
       answer = [[0 for _ in range(tmp)] for row in range(t)]
       
# 그룹 함수 
# 방문하지 않고 n-1번째 수와 같지 않으면 그룹함수를 어기는 조건이 됨
# BOJ 1316
[그룹체커](https://github.com/LeeJin0527/Algorithm/blob/master/BaekJoon/%EB%AC%B8%EC%9E%90%EC%97%B4/1316%20%E1%84%80%E1%85%B3%E1%84%85%E1%85%AE%E1%86%B8%20%E1%84%83%E1%85%A1%E1%86%AB%E1%84%8B%E1%85%A5%20%E1%84%8E%E1%85%A6%E1%84%8F%E1%85%A5.py)

# 펠린드롬 
펠린드롬은 문자열의 길이가 1일 때도 고려해야함 

# input() 으로 초기화 하기
        n, m = map(int, input().split())
        answer = [list(map(int,input())) for _ in range(n)]
        print(answer)
        
 # 가중치 있는 것은 꼭 BFS 이용해야함 
