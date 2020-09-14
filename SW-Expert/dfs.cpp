#include<iostream>
#include<cstring>
using namespace std;
int arr[1001];
bool visit[1001];
int Count = 0;
//방문했을때의 배열 만들기 
//처음에 bool false로 모두 초기화 
//그전에 방문했으면 방문처리 하고 방문 안함 
//그전에 방문 안했으면 방문처리 하고 dfs 
void dfs(int index,int sta ) {

	visit[index] = true;

	if (arr[index] == sta) {
		Count++;
		return;
	}

	
	index = arr[index];
	dfs(index,sta);

}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T, N;
	
	cin >> T; //2입력
	for (int i = 0; i < T; ++i) {
		memset(visit, false, sizeof(visit));
		Count = 0;
		cin >> N; //배열 원소 개수 넣기 
		for (int i = 1; i <= N; ++i) {
			cin >> arr[i]; //배열 원소 개수만큼 배열원소 넣기 
		}
		
		for (int j = 1; j <= N; ++j) {
			if (visit[j] == true) continue;
			dfs(j, j);
		}
		
		cout << Count << endl;
	}
	

}