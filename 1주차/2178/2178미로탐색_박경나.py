from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    dq = deque()
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()
        for i in range(4): # 4방향 체크
            nx, ny = x+dx[i], y+dy[i] # 다음 이동할 곳의 x좌표, y좌표
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 미로 범위 벗어난지 체크
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 지나온 길임을 표시
                dq.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))
