'''
from itertools import permutations
n, M, h = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

mints = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            mints.append((i, j))
        elif maps[i][j] == 1:
            home = (i, j)
        
MAX = 0
for perm in list(permutations(mints, len(mints))):
    m = M
    cnt = 0
    now = home
    for x, y in perm:
        #다음 민트초코 방믄 가능한지 확인
        m -= abs(now[0]-x) + abs(now[1]-y)
        if m < 0 : 
            break
        
        #다음 민트초코에서 집까지 갈 수 있는지 확인
        if m+h < abs(x-home[0]) + abs(y-home[1]):
            break
        else :
            cnt += 1        # 먹은 민트초코 += 1
            now = (x, y)    # 현재 위치 이동
            m += h          # 민트초코를 먹고 h만큼 회복
    MAX = max(MAX, cnt)
print(MAX)
'''
from collections import deque
from copy import copy

def bfs(q, v):
    x, y = q.popleft()
    
    

n, M, h = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

mints = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            mints.append((i, j))
        elif maps[i][j] == 1:
            home = (i, j)

MAX = 0

q = deque((home))
print(q)
x = [1,2,3,4]
bfs(q, copy(x))
print(x)

print(MAX)
