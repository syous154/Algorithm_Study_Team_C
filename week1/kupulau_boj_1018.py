import sys
input = sys.stdin.readline

m, n = map(int, input().split())

chess = []
for _ in range(m):
    chess.append(input().strip())
    
def make_chess(chess_board):
    p1 = 'BW'*4
    p2 = 'WB'*4
    
    # p1 first
    cnt1 = 0
    for i, v in enumerate(chess_board):
        if i in [0, 2, 4, 6]:
            for j in range(8):
                if v[j] != p1[j]:
                    cnt1 += 1
                            
        else:   # i = [1, 3, 5, 7]
            for j in range(8):
                if v[j] != p2[j]:
                    cnt1 += 1
    
    # p2 first
    cnt2 = 0
    for i, v in enumerate(chess_board):
        if i in [0, 2, 4, 6]:
            for j in range(8):
                if v[j] != p2[j]:
                    cnt2 += 1
                            
        else:   # i = [1, 3, 5, 7]
            for j in range(8):
                if v[j] != p1[j]:
                    cnt2 += 1
                
    return min(cnt1, cnt2)

cntlist = []
for i in range(m-8+1):
    for j in range(n-8+1):
        c1 = chess[i:i+8]
        c1 = [x[j:j+8] for x in c1]
        cntlist.append(make_chess(c1))

print(min(cntlist))