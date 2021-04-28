codeup 기초 100제

100문제가 아니라 98문제가 끝이였다!!!!!!!

하하하


# 1. sep(separation) 
 

영단어 그대로, 분리하여 출력한다. 다만 분리할 (갈라놓을 문자를 지정할 수 있다.) 이것을 구분자라고 한다.

예를 들어서 아래처럼 사용 할 수 있다.

    print('S','E','P', sep='@')

출력 >>>>> S@E@P
S , E , P라는 문자열 사이에 @가 끼워넣어져 출력된다. 즉, 구분자는 @가 된다.

# 2. if 조건
    if i % 2 == 0 and i != 0:
            print(' ', end = '')
    
    print(answer[i], end= '')
if i != 0 조건 빼먹지 말기 (예외처리 중요)


# 3. conversion
## 3-1. 10진수를 16진수로 바꿔줄때는 %를 쓰고 쉼표 안쓴다
    answer = int( input())

    print('%x' %answer)

 ## 3-2. 16진수로 입력 받을때는 입력 받을때 같이 받는다 
    temp = int(answer, 16)
  
    print("%o" %temp)
 
## 3-3. 영문자를 10진수로 바꾸어 출력 ->ord 사용
 
  
     answer = ord(input())
     print(answer)
     
 ## 3-4. 10진수를 영문자로 바꾸어 출력 -> chr 사용
  
     answer = int(input())
  
     print(chr(answer))
     

   
  # 4. Decimal point
     print(format(float(answer), ".2f"))
  
  - formating ".2f" 
  
  - 반올림하여 소수 둘째자리 까지 출력
  - 
 # 5 . 인덱스 카운트 
     temp[answer2[i]] += 1
 

# 6.이중 for문

    result = [x*y for x in range(2,10)
    ...               for y in range(1,10)]

    d = [[0 for j in range(20)] for i in range(20)]



