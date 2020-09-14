#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const string& a, const string& b) { 
	return a + b > b + a;
}

string solution(vector<int> numbers) { 
	string answer = "";
	vector<string> store;

	for (int i = 0; i < numbers.size(); i++) 
             tmp.push_back(to_string(numbers[i]));

	sort(store.begin(), store.end(), compare); 
	//compare 함수로 비교 
	for (int i = 0; i < store.size(); i++) answer += store[i];

	if (answer[0] == '0')

		return "0";

	return answer;
}