'''
python3   pypy3
146096kb  165628kb
2400ms     440ms

1. 유형 :bfs
2. 풀이방법
 - 익은 토마토의 위치를 받아와서 주변에 익지 않은 토마토로 전달
 - 관심 대상이 모든 토마토가 익는데 걸리는 날짜이므로 for문을 이용해 step by step으로 토마토 전달 수행
 - 한 step이 끝날 때 종료규칙을 검사

3. 쟁점
 - 익은토마토가 주변 토마토를 익게하면 다시 그 토마토는 탐색할 필요 없음
 - 이 문제의 핵심은 "종료규칙" => 전체 익지 않은 토마토의 수와 현재 단계에서 익은 토마토의 수를 비교하여 종료규칙 설정
 - 매 step마다 2차원 list를 모두 검사하여 종료여부를 판단할 경우 시간초과 생길 수 있음

4. 종료규칙
 - 처음부터 모든 토마토가 익어있는 경우 -> 바로 종료, 0
 - 처음부터 익은 토마토가 없는 경우 -> 바로 종료, -1
 - 모든 토마토가 익었을 경우 -> 익을때 까지 걸리는 시간
 - 익지 않은 토마토가 남았는데, 한 step동안 익은 토마토가 없는 경우 -> 종료 -1


'''

from collections import deque

n,m = map(int,input().split()) # 세로 가로
graph = [list(map(int,input().split())) for _ in range(m)]



nonTomato = 0 #익지않은 토마토의 수
tomato = [] #익은 토마토의 위치
for i in range(m):
    for j in range(n) :
        if graph[i][j] == 0 :
            nonTomato += 1
        elif graph[i][j] == 1 :
            tomato.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    global nonTomato
    answer = 0  # 토마토가 모두 익는데 걸리는 일수

    if nonTomato == 0 : #종료규칙 1번
        return answer
    if tomato == [] : #종료규칙 2번
        return -1
    q = deque(tomato)

    '''step'''
    while q :
        answer += 1
        cnt = 0 #현재 step에서 익게된 토마토의 수
        for _ in range(len(q)) :
            x,y = q.popleft()

            for idx in range(4) :
                nx,ny = x + dx[idx] , y + dy[idx]
                if nx < 0 or nx >= m or ny <0  or ny >= n : continue
                if graph[nx][ny] == -1 : continue
                if graph[nx][ny] == 0 : #안 익은 토마토가 있다면
                    graph[nx][ny] = 1
                    q.append((nx,ny))
                    cnt += 1
                    nonTomato -= 1

        #종료규칙
        if nonTomato == 0 : #종료규칙 3번
            return answer

        elif nonTomato != 0 and cnt == 0 : #종료규칙 4번
            return -1


print(bfs())






