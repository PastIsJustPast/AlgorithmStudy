#kb     ms      lang
#97968	2072	Python 3
#159240	468	    PyPy3 

#s1_q7576.py
import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
m, n = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maps = [list(map(int, input().split())) for _ in range(n)]
tomatos = 0

#BFS
def bfs(tomatos):
    day = 0
    while q:
        #남은 [안익은 토마토]가 없으면 종료
        if tomatos == 0 :
            return day

        # 아래 range(q)만큼 실행하면 오늘할 [영향끼침]을 끝낸것이므로 하루를 +1 함
        day+=1
        
        # 현재 큐의 길이가 [오늘 영향을 끼칠 토마토]의 수
        for _ in range(len(q)):    
            x, y = q.popleft()
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
                    #토마토가 익는다 -> [안익은 토마토]의 수가 -1 된다
                    # ->[내일 영향을 끼칠 토마토] 큐에 추가
                    maps[nx][ny] = 1
                    tomatos-=1
                    q.append((nx, ny))
    return -1

q = deque()
# 익은 토마토(q), 익지 않은 토마토의 수(tomatos) 탐색
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 :
            q.append((i, j))
        elif maps[i][j] == 0 :
            tomatos+=1

print(bfs(tomatos))