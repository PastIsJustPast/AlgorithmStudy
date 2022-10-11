from collections import deque

n,m,k = map(int,input().split())
#input_cell = [list(map(int,input().split())) for _ in range(n)]
input_cell = []
for info in input().split("\n"):
    input_cell.append(list(map(int,info.split())))

graph = [[ [-1,-1] for _ in range(m + 2 * k)] for _ in range(n + 2 * k)]
nonActive = deque()
active = deque()

for r in range(n):
    for c in range(n):
        x = input_cell[r][c]
        if x > 0 :
            graph[r + k][c + k ] = [x,0] #생명력, 세포가 배양된 시간
            nonActive.append([(r + k, c + k),(x,x)])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = 1

for t in range(1, k + 1) :
    t += 1
    activeSize = len(active) #미리 길이를 체크해야함

    #비활성화 시간 감소
    for i in range(len(nonActive)) :
        pos,life = nonActive.popleft()
        if life[1] == 1: #생명력이 1이 남았으면
            active.append([pos,(life[0],life[0]),True]) #위치, 생명력, 남은생명력,복제 가능한 여부
        else :
            nonActive.append([pos,(life[0],life[1] - 1)])

    #활성화 체크
    temp = []
    for i in range(activeSize) : #기존에 있던 만큼만 활성화
        pos,life,isCopy = active.popleft()
        #복제 가능여부 체크
        if isCopy  : #복제가 되어야 한다면
            temp.append([pos,life[0]])
        #활성화 시간 감소
        if life[1] ==1 : #죽기 직전이라면
            continue
        else :
            active.append([pos,(life[0],life[1] - 1),False])

    #복제
    for pos,life in temp :
        r,c = pos
        for i in range(4):
            nr,nc = r + dx[i], c + dy[i]
            if graph[nr][nc][1] == -1 : #아직 빈칸이라면
                graph[nr][nc] = [life, t]
                nonActive.append([(nr,nc), (life, life)])

            elif graph[nr][nc][1] < t : #이미 있다면 pass
                continue

            elif graph[nr][nc][1] == t :
                max_life = max(graph[nr][nc][0] , life)
                graph[nr][nc] = [max_life,t]
                nonActive.append([(nr,nc),(life,life)])

active
len(nonActive)