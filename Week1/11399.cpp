#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    
    int n;
    cin >> n;
    vector<int> line;

    for(int i =0; i < n ; i++){
        int val;
        cin>>val;
        line.push_back(val);
    }

    sort(line.begin(), line.end()); //오름 차순으로 정렬되어 있을 때가 최소

    int sum = 0;
    for(int i = n ; i >= 0 ; i--){
        for(int j = 0; j < i; j++){
            sum += line[j];     // 마지막 사람이 걸리는 시간부터 하나씩 계산하여 sum에 누적합
        }
    }

    cout << sum << '\n';

    return 0;
}   
