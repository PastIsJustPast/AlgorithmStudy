import sys
sys.stdin = open('sample.txt')


from collections import deque

N, M = map(int, input().split())
MAP = []
for _ in range(N):
    MAP.append(input())
discover = [[0 for _ in range(M)] for _ in range(N)]
Q = deque()
Q.append((0, 0, 1))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
while Q:
    x, y, step = Q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if discover[nx][ny] or MAP[nx][ny] == '0':
                continue
            if nx == N -1 and ny == M - 1:
                print(step + 1)
                exit(0)
            discover[nx][ny] = 1
            Q.append((nx, ny, step+1))
