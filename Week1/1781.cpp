#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>         // 우선순위 큐를 쓰기 위해 필요

using namespace std;

// 문제에서 주어진 정렬 방식대로 pair를 정렬하기 위해 사용하는 함수입니다.
// (데드라인 오름차순, 데드라인이 같다면 컵라면 수가 작은 것이 앞으로)
int cmp(const pair<int, int>& a, const pair<int, int>& b) {
    if(a.first == b.first) {
        return a.second < b.second; 
    }
    return a.first < b.first;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<pair<int, int>> homework;

    for(int i = 0; i < n; i++){
        int d, r;
        cin >> d >> r;
        homework.push_back({d, r});
    }
    // 데드라인 기준 정렬
    sort(homework.begin(), homework.end(), cmp);

    // 최소 힙(오름차순 정렬) 우선순위 큐
    priority_queue<int, vector<int>, greater<int>> pq;
    int sum = 0;

    for(int i = 0; i < n; i++) {
        // 현재 문제의 컵라면 수를 큐에 넣는다
        pq.push(homework[i].second);

        // 만약 우선순위 큐(해결한 문제 목록) 크기가 현재 문제의 데드라인보다 크면
        // 가장 컵라면 수가 작은 문제 하나를 제거한다
        if((int)pq.size() > homework[i].first) {
            pq.pop();
        }
    }

    // 우선순위 큐에 남아 있는(해결한) 문제들의 컵라면 수를 모두 더한다
    while(!pq.empty()) {
        sum += pq.top();
        pq.pop();
    }

    cout << sum << '\n';
    return 0;
}