# 1.4130775928497314
import heapq
import sys

n = int(input())
li = []
[heapq.heappush(li, list(map(int, input().split()))) for _ in range(n)]
l, p = map(int, input().split())
cnt = 0
heap = []

while p < l:
    while li and li[0][0] <= p:
        a, b = heapq.heappop(li)
        heapq.heappush(heap, [-b, a])
    if not heap:
        print(-1)
        sys.exit(0)
    b, a = heapq.heappop(heap)
    p += -b
    cnt += 1
print(cnt)