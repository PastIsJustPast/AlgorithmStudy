'''
유형 : BFS

풀이 방법
- 시작 위치로부터 도달할 수 있는 모든 칸에 시작위치부터 그 깐까지의 거리를 기입


'''


from collections import deque
n,m = map(lambda x : int(x) -1 , input().split()) #행,열
'''graph = []
for info in input().split("\n"):
    graph.append(list(map(int,list(info))))
'''
graph =[]
for _ in range(n+1):
    graph.append(list(map(int,list(input()))))

#dist matrix생성 : 시작 위치(0,0)부터 각 위치까지의 거리
nrow = len(graph)
ncol = len(graph[0])
dist = [[0] * ncol for _ in range(nrow)]
dist[0][0] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

#dfs 함수
def bfs() :
    x,y = 0,0 #시작 위치

    q = deque()
    q.append((x,y))

    while q :
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x +dx[i] , y + dy[i]

            #예외 규칙
            if nx < 0 or nx >= nrow or ny < 0 or ny >= ncol : continue
            if graph[nx][ny] == 0 or dist[nx][ny] != 0 : #갈 수 없거나 이미 방문한 곳이면
                continue

            dist[nx][ny] = dist[x][y] + 1 #시작 지점부터 (x,y)까지의 최단거리 + 1
            q.append((nx,ny))


bfs()
print(dist[n][m])