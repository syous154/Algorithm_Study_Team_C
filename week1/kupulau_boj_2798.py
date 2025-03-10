from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
list1 = list(map(int, input().split()))

combi = list(combinations(list1, 3))
combi1 = [sum(x) for x in combi]
offset1 = [x for x in combi1 if x<=m]
offset2 = [m-x for x in offset1] 
offset2.sort()
print(m-offset2[0])