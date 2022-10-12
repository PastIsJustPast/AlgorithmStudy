import sys


sys.stdin = open('../../../ArgorithmStudy/5주차(삼성)/5653_줄기세포배양/sample_input.txt')


from collections import deque


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    board_size = 2 * (K + max(N, M))
    visit = [[False for _ in range(board_size)] for _ in range(board_size)]
    Q = deque()
    for i in range(N):
        line = map(int, input().split())
        for j, life in enumerate(line):
            if life:
                Q.append((K+i, K+j, life, 0))
                visit[K+i][K+j] = True
    for _ in range(K):
        candidates = {}
        for _ in range(len(Q)):
            x, y, life, lived = Q.popleft()
            if lived == life:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if not visit[nx][ny]:
                        if (nx, ny) not in candidates:
                            candidates[(nx, ny)] = life
                        else:
                            candidates[(nx, ny)] = max(life, candidates[(nx, ny)])
            if lived < 2 * life - 1:
                Q.append((x, y, life, lived + 1))

        for k, life in candidates.items():
            x, y = k
            Q.append((x, y, life, 0))
            visit[x][y] = True
    answer = len(Q)
    print(f'#{t} {answer}')