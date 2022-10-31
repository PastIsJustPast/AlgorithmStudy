"""
python    pypy
32580kb 117068kb
656ms    248ms
"""

from collections import deque
n,m,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)] #n * m


def nxt_bottom(d) :
    global dice
    if d == 0 :
        dice[0].rotate(1)
        dice[1][3] = dice[0][3]
        dice[1][1] = dice[0][1]
    elif d == 2 :
        dice[0].rotate(-1)
        dice[1][3] = dice[0][3]
        dice[1][1] = dice[0][1]
    elif d == 1 :
        dice[1].rotate(1)
        dice[0][3] = dice[1][3]
        dice[0][1] = dice[1][1]
    else :
        dice[1].rotate(-1)
        dice[0][3] = dice[1][3]
        dice[0][1] = dice[1][1]
    return dice[0][3]


'''점수계산
bfs 
'''
dx = [0,1,0,-1] #동남서북
dy = [1,0,-1,0]
def bfs(sx,sy) :
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[sx][sy] = True
    q = deque()
    q.append((sx,sy))
    cnt = 1
    while q :
        x,y = q.popleft()
        value = graph[x][y]
        for i in range(4):
            nx,ny = x + dx[i] , y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == True :  continue
            if graph[nx][ny] == value :
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt += 1
    return cnt


#주사위
dice = []
dice.append(deque([4,1,3,6])) #가로
dice.append(deque([2,1,5,6])) #세로


total = 0
sx,sy = 0,0
d= 0
bottom = 6

for _ in range(k) :
    '''이동할 위치 탐색'''
    nx,ny = sx + dx[d], sy + dy[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= m :
        if d == 0 : d = 2
        elif d == 1 : d = 3
        elif d == 2 : d = 0
        else : d = 1
        nx,ny = sx + dx[d], sy + dy[d]

    '''이동'''
    sx,sy = nx,ny

    '''점수계산'''
    total += graph[sx][sy] * bfs(sx,sy)
    '''방향갱신'''
    bottom = nxt_bottom(d)
    if  bottom > graph[sx][sy] :
        d = (d + 1 ) % 4
    elif bottom < graph[sx][sy] :
        d = (d + 3 ) % 4


print(total)

