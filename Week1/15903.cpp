#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(0);
	  cin.tie(0);

    int n, m;
    cin>>n>>m;

    vector<long long> card(n);
    for(int i = 0; i < n ; i++){
        cin>>card[i];
    }

    while(m--){
        sort(card.begin(), card.end()); // 반복적으로 정렬을 진행하여 가장 작은 2개의 값을 더하도록한다.

        long long val = card[0] + card[1];  // 계속 값이 더해지기 때문에 int가 아닌 long long를 사용해야한다.
        card[0] = val;                      // 덮어쓰기 동작
        card[1] = val;                      // 덮어쓰기 동작

    }

    long long result = 0;   
    for(int i = 0 ; i < n ; i++){
        result += card[i];
    }

    cout<<result<<'\n';

    return 0;
}   
