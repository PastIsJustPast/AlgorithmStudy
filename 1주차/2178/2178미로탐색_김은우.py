#s1_q2178.py
from collections import deque
n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]
dist[0][0] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1  :
            print(dist[x][y])    #목적지에 도착한다면 print 후 종료.
            return
        for d in range(4):    # 4 방향을 순차적으로 탐색
            nx = x+dx[d]
            ny = y+dy[d]
            #갈 수 있는 곳이며 방문한 적이 없는곳이라면 Queue에 추가
            if nx >= 0 and nx < n and ny >= 0 and ny < m and maps[nx][ny] == 1 and not dist[nx][ny]:
                dist[nx][ny] = dist[x][y]+1
                q.append((nx, ny))

bfs()