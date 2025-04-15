from collections import Counter
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())   # 세로, 가로, 블록 수

ground = []
for _ in range(n):
    ground.extend(map(int, input().split()))

height_count = Counter(ground)
min_time = float('inf')
best_height = 0

for target in range(min(ground), max(ground)+1):
    remove_blocks = 0   # 없앨 블록
    add_blocks = 0    # 쌓을 블록
    
    for height, count in height_count.items():
        if height > target:
            remove_blocks += (height-target)*count
        elif height < target:
            add_blocks += (target-height)*count
            
    if remove_blocks + b >= add_blocks:
        time = remove_blocks*2 + add_blocks
        if time <= min_time:
            min_time = time
            best_height = target
            
print(min_time, best_height)