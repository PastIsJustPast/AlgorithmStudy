'''
메모리    시간
32596KB	604ms

BFS
'''

from collections import deque

def move(dir):
    global dice
    if dir == right: # 오른쪽
        tmp = dice[1][2]
        dice[1] = [dice[3][1], dice[1][0], dice[1][1]] # 6 4 1
        dice[3][1] = tmp
    elif dir == left: # 왼쪽
        tmp = dice[1][0]
        dice[1] = [dice[1][1], dice[1][2], dice[3][1]] # 1 3 6
        dice[3][1] = tmp
    elif dir == up: # 위쪽
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp
    elif dir == down: # 아래쪽
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp

def bfs(y, x, B):
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    dq = deque()
    dq.append((y, x))
    visited[y][x] = 1
    while dq:
        y, x = dq.pop()
        cnt += 1
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx]:
                continue
            if num[ny][nx] == B:
                visited[ny][nx] = 1
                dq.append((ny, nx))
    return cnt*B

n,m,k = map(int, input().split())
dx = [0,-1,0,1]
dy = [-1,0,1,0]
dice = [
    [0,2,0],
    [4,1,3],
    [0,5,0],
    [0,6,0]
]
num = [list(map(int, input().split())) for _ in range(n)]
up, left, down, right = 0,1,2,3
dir = right
cur = [0, 0]
result = 0

for _ in range(k):
    ny, nx = cur[0]+dy[dir], cur[1]+dx[dir]

    if ny < 0 or ny >= n or nx < 0 or nx >= m:
        dir = (dir+2) % 4
        ny, nx = cur[0] + dy[dir], cur[1] + dx[dir]

    cur = [ny, nx]
    move(dir)
    B = num[ny][nx]
    score = bfs(ny, nx, B)
    result += score

    A = dice[3][1]
    if A > B:
        dir = (dir-1) % 4 # 시계
    elif A < B:
        dir = (dir+1) % 4 # 반시계

print(result)