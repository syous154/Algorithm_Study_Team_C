def min_time(Pi):

    # 문제 풀이 알고리즘
    # 인출을 빨리 할 수 있는 사람부터 먼저 인출하도록 하면 가장 빠르다.
    # 1. Pi 리스트를 오름차순으로 정렬한다.
    # 2. 정렬된 Pi 리스트에서 누적 합을 계산한다.

    Pi.sort()
    wait_time = 0
    total_time = 0

    for time in Pi:
        wait_time += time
        total_time += wait_time
    
    return total_time 

N = int(input())
Pi = list(map(int, input().split()))

print(min_time(Pi))