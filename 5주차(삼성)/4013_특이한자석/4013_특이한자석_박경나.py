# 회전 주의
# 좌우 dfs
# rotate ...ㅎㅎ
from collections import deque

def dfs(cur, d):
    visited[cur] = 1

    if d == 1: # 시계
        #magnet[cur].appendleft(magnet[cur].pop())
        magnet[cur].rotate(1)
        if 0 <= cur+1 <= 3 and not visited[cur+1]:
            if magnet[cur][3] != magnet[cur+1][6]: # 회전하기 전 2
                dfs(cur+1, -1)
        if 0 <= cur-1 <= 3 and not visited[cur-1]:
            if magnet[cur][7] != magnet[cur-1][2]: # 회전하기 전 6
                dfs(cur-1, -1)
    else: # 반시계
        #magnet[cur].append(magnet[cur].popleft())
        magnet[cur].rotate(-1)
        if 0 <= cur+1 <= 3 and not visited[cur+1]:
            if magnet[cur][1] != magnet[cur + 1][6]: # 회전하기 전 0
                dfs(cur+1, 1)
        if 0 <= cur-1 <= 3 and not visited[cur-1]:
            if magnet[cur][5] != magnet[cur-1][2]: # 회전하기 전 6
                dfs(cur-1, 1)

def scr():
    global total
    for i in range(4):
        total += magnet[i][0] * (2**i)

t = int(input())
for i in range(t):
    k = int(input())
    magnet = [deque(map(int, input().split())) for _ in range(4)]
    for _ in range(k):
        n, rt = map(int, input().split())
        visited = [0] * 4
        dfs(n-1, rt)
    total = 0
    scr()
    print("#{} {}".format(i+1, total))