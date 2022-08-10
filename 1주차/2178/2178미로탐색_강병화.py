from collections import deque
import sys

si = sys.stdin.readline

N, M = map(int, si().split())
board = []
for _ in range(N):
    board.append(list(map(int, input())))
visited = [[False] * M for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def BFS():
    global visited
    q = deque([(0,0,1)])
    visited[0][0] = True
    while q:
        cy, cx, cdist = q.popleft()
        if cy == N - 1 and cx == M - 1:
            return cdist
        for dy,dx in direction:
            ny = cy + dy
            nx = cx + dx
            if ny < 0 or nx < 0 or ny >= N or nx >= M :continue
            if visited[ny][nx] : continue
            if board[ny][nx] == 0: continue
            visited[ny][nx] = True
            q.append((ny, nx, cdist + 1))
    return -1
print(BFS())
