def solution(board, skill):
    n, m = len(board), len(board[0])    
    
    maps = [[0 for _ in range(m+1)] for _ in range(n+1)]
    # 누적합 기준으로 board 설정
    for i in range(n):
        for j in range(m-1, 0, -1):
            board[i][j] -= board[i][j-1]
    
    for j in range(m):
        for i in range(n-1, 0, -1):
            board[i][j] -= board[i-1][j]
    
    for i in board:
        print(i)
        
    for s in skill: 
        t, r1, c1, r2, c2, degree = s
        # 철거라면 빼기 설정
        if t == 1 :
            degree *= -1

        maps[r1][c1] += degree
        maps[r2][c1+1] -= degree
        maps[r1][c2+1] -= degree
        maps[r2+1][c2+1] -= degree
            
    for i in board:
        print(i)
    
    # 누적합 계산
    for i in range(n):
        for j in range(1, m):
            maps[i][j] += maps[i][j-1]
    
    for j in range(m):
        for i in range(1, n):
            maps[i][j] += maps[i-1][j]
            
    answer = 0
    
    # 누적합 표기 -> 직접 표기 변경
    for i in range(n):
        for j in range(-1, m-1, -1):
            board[i][j] -= board[i][j+1]
    
    for j in range(m):
        for i in range(-1, n-1, -1):
            board[i][j] -= board[i+1][j]
    
    #파괴되지 않은 건물 수 확인
    answer = 0
    for i in board :
        answer += len([j for j in i if j > 0])    
    return answer


board, skill, result = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]], 10
print(solution(board, skill))
board, skill, result = [[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]], 6
print(solution(board, skill))