import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))
list1.sort()

sum1 = [0]
c = 0
for x in list1:
    c += x
    sum1.append(c)
    
print(sum(sum1))