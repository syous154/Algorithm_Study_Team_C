#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>         

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;
    // 우선순위큐를 오름차순으로 정렬
    priority_queue<int, vector<int>, greater<int>> pq;

    for(int i = 0 ;i < n ; i++){
        int val;
        cin>>val;
        pq.push(val);   
    }

    int sum = 0;

    while(1){
        if(pq.size()==1){
            break;
        }
        
        // 가장 작은 수 2개를 합친다.
        int val1 = pq.top();
        pq.pop();
        int val2 = pq.top();
        pq.pop();

        // 합친 횟수를 pq에 다시 저장
        pq.push(val1 + val2);
        
        // 합친 횟수를 누적합 
        sum += val1 + val2;

    }

    cout<<sum<<'\n';
    
    return 0;
}