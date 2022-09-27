import sys


sys.stdin = open('sample_input.txt')


from collections import deque
from copy import deepcopy


def get_top_idx(board):
    H = len(board)
    W = len(board[0])
    idx = []
    for j in range(W):
        for i in range(H):
            if board[i][j]:
                idx.append((i, j))
                break
    return idx


def break_brick(i, j, board):
    board = deepcopy(board)
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        dist = board[x][y] - 1
        board[x][y] = 0
        if dist > 0:
            for nx in range(max(0, x - dist), min(H, x + dist + 1)):
                if board[nx][y]:
                    q.append((nx, y))
            for ny in range(max(0, y - dist), min(W, y + dist + 1)):
                if board[x][ny]:
                    q.append((x, ny))
    return board


def apply_gravity(board):
    H = len(board)
    W = len(board[0])
    new_board = []
    for j in range(W):
        q = deque()
        for i in range(H):
            if board[i][j]:
                q.append(board[i][j])
            else:
                q.appendleft(0)
        new_board.append(list(q))
    new_board = [list(line) for line in zip(*new_board)]
    return new_board


def dfs(board, n):
    if n == N:
        cnt = 0
        for line in board:
            for elt in line:
                if elt:
                    cnt += 1
        return cnt
    dfs_ret = []
    indexes = get_top_idx(board)
    if not indexes:
        return 0
    for i, j in indexes:
        new_board = break_brick(i, j, board)
        new_board = apply_gravity(new_board)
        dfs_ret.append(dfs(new_board, n + 1))
    return min(dfs_ret)


T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    board = []
    for _ in range(H):
        board.append([int(x) for x in input().split()])
    indexes = get_top_idx(board)
    answer = dfs(board, 0)
    print(f'#{t} {answer}')
    