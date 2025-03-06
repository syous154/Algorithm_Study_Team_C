#include <iostream>
#include <vector>

using namespace std;

int main() {
    
    int n;
    cin>>n;

    vector<int> v(n);
    for(int i = 0 ; i < n ; i++){
        cin>>v[i];
    }

    int result = 0;
    for(int i = 1; i < n-1; i++){  // 처음과 마지막이 아닌 탑 중에
        int val = min(v[i-1], v[i+1]);  // 주변의 탑의 최소 크기를 구해서

        if(result < val + v[i]){  // 현재 탑과 더한다. 이 값이 현재 탑이 커질 수 있는 최댓값이다.
            result = val + v[i];
        }

    }
    if (result < v[0] || result < v[n-1]){  // 첫번쨰 탑과 마지막 탑이 가장 높은 경우를 생각해주어야한다. 
        result = max(v[0], v[n-1]);         // ex) 100 1 1 1 2
    }
    cout << result << '\n';
    return 0;
}   
