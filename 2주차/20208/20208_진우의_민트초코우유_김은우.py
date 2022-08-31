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
import sys
input = sys.stdin.readline

def dfs(x, y):
    global MAX, visited, m, h, mints, hx, hy, c, visited_cnt
    
    for i in range(c) :
        nx, ny = mints[i]
        cost = abs(x-nx) + abs(y-ny)
        
        if not visited[i] and m >= cost:    
            visited[i]  = 1
            visited_cnt += 1
            m -= cost - h
            dfs(nx, ny)
            m += cost - h
            visited_cnt -= 1
            visited[i] = 0
        elif m >= abs(x-hx) + abs(y-hy):
            MAX = max(MAX, visited_cnt)

n, m, h = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited_cnt = 0
mints = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            mints.append((i, j))
        elif maps[i][j] == 1:
            hx, hy = i, j
c = len(mints)
visited = [0 for _ in range(c)]

MAX = 0
dfs(hx, hy)
print(MAX)
