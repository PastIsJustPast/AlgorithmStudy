import sys
from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dq = deque()
ans = 0

# dq 초기 토마토 위치 좌표
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            dq.append((i, j))

while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                dq.append((nx, ny))

for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit(0)
    ans = max(ans, max(i))
print(ans-1)