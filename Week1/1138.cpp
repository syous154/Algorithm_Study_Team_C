#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    
    int n;
    cin>>n;
    vector<int> bigger;
    vector<int> line(n, 0);

    for(int i = 0 ; i < n ; i++){
        int val;
        cin>>val;
        bigger.push_back(val);
    }

    for(int i = 0 ; i < n ; i++){
        int count = 0;
        for(int j = 0; j < n ; j++){
            if(line[j] == 0){   // 사람이 서 있지 않은 자리일 때
                if(count == bigger[i]){ // 왼쪽에 큰사람이 있는 수만큼 띄고 자리를 잡는다.
                    line[j] = i+1;
                    break;
                }
                count++;
            }
        }
    }
    for(int i = 0; i < n ; i++){
        cout<<line[i]<<' ';
    }
    return 0;
}   
