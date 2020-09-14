#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
//[6, 10, 2]	"6210"
//[3, 30, 34, 5, 9]  "9534330"
//자리수가 몇개이든 일단 맨 앞자리 비교해서 넣기 
//6 2 1 0 두자리수 이상이면 배열 잘라서 넣기 그리고 넣기 
//9 5 자리수가 같은 수가 있다? 자르고 비교 그 다음 수가 원래 자리수보다 크면 그 다음수먼저 아니면 그냥 넣기 
//return answer;
// numbers_len은 배열 numbers의 길이입니다.
char* solution(int numbers[], size_t numbers_len) {
	// return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
	char* answer = (char*)malloc(1);
	return answer;
	char s1[5];
	sprintf(s1, "%d", numbers);
	printf("%s", s1);
}

