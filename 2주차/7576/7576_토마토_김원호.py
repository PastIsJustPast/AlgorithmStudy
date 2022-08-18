# python3 153628 KB, 3032 ms
# pypy3 251552 KB, 600 ms

from collections import deque

M, N = map(int, input().split())
box = [[int(x) for x in input().split()] for _ in range(N)]
discover = [[0 for _ in range(M)] for _ in range(N)]
riped_tomatos = []
for i in range(N):
    for j in range(M):
        if box[i][j] == -1:
            discover[i][j] = 1
        elif box[i][j] == 1:
            discover[i][j] = 1
            riped_tomatos.append((i, j, 0))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
Q = deque(riped_tomatos)
while Q:
    x, y, day = Q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if discover[nx][ny]:
                continue
            discover[nx][ny] = 1
            Q.append((nx, ny, day+1))

discover_cnt = sum(map(sum, discover))
if discover_cnt != M * N:
    print(-1)
else:
    print(day)