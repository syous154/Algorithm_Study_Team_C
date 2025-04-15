import sys
input = sys.stdin.readline

n = int(input())
order = list(map(int, input().split()))

answer = [0] * n  

for i in range(1, n+1):  
    count = order[i-1]  
    for j in range(n): 
        if answer[j] == 0:  
            if count == 0: 
                answer[j] = i  
                break
            count -= 1  

print(*answer)