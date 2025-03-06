#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(int first, int second){    // 내림차순 정렬을 위한 cmp 함수
    return first > second;    
}

int main() {
    
    int n;
    cin>>n;
    vector<int> a, b;

    for(int i = 0; i < n ; i++){
        int val;
        cin>>val;
        a.push_back(val);
    }
    for(int i = 0; i < n ; i++){
        int val;
        cin>>val;
        b.push_back(val);
    }
    // S의 값이 최소가 되는 경우는 a의 최소와 b의 최대가 곱해져야 한다고 가정

    sort(a.begin(), a.end());       // 오름차순 정렬
    sort(b.begin(), b.end(), cmp);  // cmp 함수를 이용해 내림차순 정렬

    int S = 0;
    for(int i = 0 ; i < n ; i++){
        S += (a[i] * b[i]);
    }

    cout << S << '\n';

    return 0;
}   
