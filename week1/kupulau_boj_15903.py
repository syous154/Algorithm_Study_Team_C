# First trial
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(m):
    cards.sort()
    new = cards[0]+cards[1]
    cards[0], cards[1] = new, new
    
print(sum(cards))

# Second trial
# Using heapq is more efficient
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

for _ in range(m):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    new = a + b
    heapq.heappush(cards, new)
    heapq.heappush(cards, new)
    
print(sum(cards))