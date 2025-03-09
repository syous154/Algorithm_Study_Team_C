from itertools import combinations

def distance3(a, b, c):
    diff1 = 0
    for i in range(4):
        if a[i]!=b[i]:
            diff1 += 1
        if b[i]!=c[i]:
            diff1 += 1
        if a[i]!=c[i]:
            diff1 +=1
    return diff1

t = int(input())
for _ in range(t):
    n = int(input())
    mbti = input().split()
    
    if n >= 33:
        print(0)
    else:
        combi = list(combinations(mbti, 3))
    
        min_dist = 100
        for x in combi:
            min_dist = min(min_dist, distance3(x[0], x[1], x[2]))
    
        print(min_dist)