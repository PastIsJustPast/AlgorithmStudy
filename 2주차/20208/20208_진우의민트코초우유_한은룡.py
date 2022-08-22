'''
pypy3
126952kb
3000ms

풀이방법
- 백트래킹을 활용하여 품
- 현재 위치에서 민트초코 우유로 이동할 수 있으면 이동하고, 더이상 이동할 수 없지만 집으로는 되돌아 올 수 있는 경우에는 민트초코를 갱신

쟁점
- 종료규칙이 매우 어려움 -> 매번 집에 돌아올 수 있는지 탐색하면 시간초과
 => 최대로 민트초코 우유를 먹는것이 관건이므로 더 이상 갈 곳이 없을 때 집으로 돌아올 수 있는지 확인

- 갱신 타이밍이 어려움 -> 더이상 갈 곳이 없을 때 마다 우유를 마신 최대 횟수를 갱신할 경우 집으로 돌아오지 않는 경우도 갱신됨
   => 더 이상 갈 수 없지만 집에 올 수 있는 경우에 갱신

'''


n,m,h = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

''' 우유 위치와 집 위치'''
milk = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2 :
            milk.append((i,j))
        elif graph[i][j] == 1 :
            home = (i,j)

'''거리 계산 함수'''
def cal(b,f):
    return abs(b[0] - f[0]) + abs(b[1] -f[1])

hp = m
cnt = 0
max_cnt = 0
visited = [False] * len(milk) #index번째 민트초코 방문 여부
def backTracking(x,y) : #현재 위치
    global hp,cnt,max_cnt,visited

    for i in range(len(milk)):
        nx,ny = milk[i]#다음 위치
        if visited[i] == False and cal((x,y),(nx,ny)) <= hp :# and check_move((x,y),(nx,ny),hp):  #방문가능하고, 현재 체력으로 갈 수 있고, 다시 집으로 돌아올 수 있다면
            visited[i] = True #방문처리하고
            hp += h #체력 회복
            hp -= cal((x,y),(nx,ny)) #이동한 만큼 감소
            cnt += 1
            backTracking(nx,ny)
            cnt -= 1
            hp += cal((x,y),(nx,ny)) #이동한 만큼 다시 회복
            hp -= h #회복한만큼 감소
            visited[i] = False
        elif cal((x,y),home) <= hp: #갈 곳은 없지만 집으로 갈 수 있다면
            max_cnt = max(cnt,max_cnt)

        else : pass #집으로도 못가고 갈곳도 없다면 그냥 끝, 갱신도 없음

backTracking(home[0],home[1])
print(max_cnt)



'''
경유지들이 나타났을 때 이동가능여부를 return 한다.
input : 현재위치, 다음 위치, 현재 체력
return : True False 
'''

def check_move(b,f,nh):
    dist1 = cal(b,f) #현재 위치에서 다음 목적지까지의 거리
    if dist1 <=  nh : #현재 체력으로 갈 수 있다.
        dist2 = cal(f,home) #다음목적지에서 집까지의 거리
        if dist2 <=  nh - dist1 + h: #회복후에 다시 집까지 갈 수 있다.
            return True
        else: False
    else : return False