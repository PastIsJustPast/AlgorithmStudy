"""
문제풀이법
좌표로 풀고 돌아가면서 푼다고는 생각했지만, 3차원 배열은 생각해본적이 없어서 고민하다가 검색해보고 알았음 참고 -> https://prgms.tistory.com/101
방향, 좌표 풀이가 헷갈려서 구현 문제 다시 풀어봄 -> https://github.com/ndb796/python-for-coding-test/tree/master/4 
수도코드 이해하고 비슷하게 짜려고 했음
입력 리스트로 좌표 만들고 돌면서 방문했는지 찾음
각 점에서 같은 방향으로 나가야만이 루프가 생김

어려웠던점
시간복잡도가 왜 O(n^2)인지,,
아직도 행렬, 좌표 y,x 가 헷갈린다.. 근데 예전에 책에도 똑같이 써놓음ㅎ + 여기서는 시계, 반시계 방향도, 돌아도 같은 곳으로 오는것도,,,
"""

#     ↓  ←   ↑  →
dx = (0, -1, 0, 1)
dy = (1, 0, -1, 0)

 
def solution(grid):
    answer = []
    lx, ly =  len(grid[0]), len(grid)
    
    # 4방향 방문 기록 리스트 : y*x*4
    visited = [[[False] * 4 for _ in range(lx)] for _ in range(ly)]

    # 모든 좌표에 대하여 탐색 [0][0], [0][1], [1][0], [1][1]
    for y in range(ly):
        for x in range(lx):
            # (y, x) 좌표에 대해 4방향 탐색
            for d in range(4):
                # 해당 좌표-방향 이 기존에 사용된 경우
                if visited[y][x][d]:
                    continue
                # 사용되지 않은 좌표-방향인 경우
                count = 0
                ny, nx = y, x
                
                # 빛을 이동 시켜가며 탐색
                while not visited[ny][nx][d]:
                    visited[ny][nx][d] = True
                    count += 1
                    if grid[ny][nx] == "S": # S의 경우 방향 변경 X
                        pass
                    elif grid[ny][nx] == "L": # L의 경우 반시계방향
                        d = (d - 1) % 4
                    elif grid[ny][nx] == "R": # R의 경우 시계방향
                        d = (d + 1) % 4
                    
                    # 좌표의 길이로 %연산을 하여 격자를 벗어난 경우에도 자리를 찾아가도록함.
                    ny = (ny + dy[d]) % ly 
                    nx = (nx + dx[d]) % lx

                answer.append(count)
    answer = sorted(answer) # 오름차순 정렬
    return answer