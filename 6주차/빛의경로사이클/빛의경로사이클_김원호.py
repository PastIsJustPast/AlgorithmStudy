def solution(grid):
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    N = len(grid)
    M = len(grid[0])
    visit = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for k in range(4):
                if visit[i][j][k]:
                    continue
                x, y, head = i, j, k
                cnt = 0
                while not visit[x][y][head]:
                    visit[x][y][head] = True
                    x = (x + dx[head]) % N
                    y = (y + dy[head]) % M
                    if grid[x][y] == 'L':
                        head = (head - 1) % 4
                    elif grid[x][y] == 'R':
                        head = (head + 1) % 4
                    cnt += 1
                answer.append(cnt)
    answer.sort()
    return answer