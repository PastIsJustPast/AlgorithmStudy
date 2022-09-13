def solution(board, aloc, bloc):
    def dfs(board, aloc, bloc, cnt, turn):
        if turn == 'A':
            nturn = 'B'
            x, y = aloc
        else:
            nturn = 'A'
            x, y = bloc
        if board[x][y] == 0:
            return cnt, nturn
        dfs_ret = []
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny]:
                    board[x][y] = 0
                    if turn == 'A':
                        dfs_ret.append(dfs(board, (nx, ny), bloc, cnt + 1, nturn))
                    else:
                        dfs_ret.append(dfs(board, aloc, (nx, ny), cnt + 1, nturn))
                    board[x][y] = 1
        if dfs_ret == []:
            return cnt, nturn
        win_case = [ret for ret in dfs_ret if ret[1] == turn]
        lose_case = [ret for ret in dfs_ret if ret[1] == nturn]
        if win_case:
            return min([ret[0] for ret in win_case]), turn
        return max([ret[0] for ret in lose_case]), nturn


    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    N = len(board)
    M = len(board[0])
    answer = dfs(board, aloc, bloc, 0, 'A')
    return answer[0]