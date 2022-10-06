"""
유형 : 완전 탐색

풀이방법 : 
- 모든 칸에 대해 손해보지 않고 최대로 들릴 수 있는 집을 모두 찾아줌
1. 모든 칸 탐색 + k를 늘려주면서 + 마름모 안에 들어오는 집 갯수를 찾으면서 + 비용을 계산하고 + 최대를 갱신 -> 아마 시간 초과
 - 매 칸마다 마름모를 찾는 것은 안될 것 같음
2. 사전에 집 위치를 리스트에 담기 + 모든 칸 탐색 + k를 늘려주면서 + 모든 집까지의 거리를 계산해서 + 거리가 (k-1)인 집을 찾고 최대를 갱신 -> 아마 시간초과
 - k를 늘려주면서 거리를 계산을 반복적으로 할 수 없을 것 같음
3. 사전에 집 위치를 리스트에 담기 + 모든 칸 탐색 + 각 칸에서 모든 집까지의 거리를 계산하고 + k를 늘려주면서 + 거리가 (k-1)보다 작은 집의 수를 찾고 최대를 갱신
 - 반복시간을 매우 아낄 수 있음
 
쟁점 : 반복 + 반복 + 반복이라 시간을 아끼는 것이 중요함

시간복잡도
모든칸 탐색 : N**2
k의 최대 길이 : N
k를 늘려주면서 마름모 안에 탐색.. 어림잡아 N**2
이 것을
모든칸 탐색 N**2에 근사적으로 줄일 수 있었음 

"""


n,m = map(int,input().split())
#graph = [list(map(int,input().split()))) for _ in range(n)]
graph = []
for info in input().split("\n"):
    graph.append(list(map(int,info.split())))

#집 위치 탐색
home = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 :
            home.append((i,j))

def calDist(n_pos,h_pos):
    """
    현재 위치와 집 까지의 거리 계산하는 함수
    :return: 거리
    """
    nx,ny = n_pos
    hx,hy = h_pos
    d = abs(nx - hx) + abs(ny - hy)
    return d

def getMoney(cnt,k):
    """
    수익을 계산하는 함수
    """
    return   (cnt * m) - (k * k  + (k-1) * (k-1))



def getMaxHome(n_pos):
    """
    현재 위치에서 손해를 보지 않고 최대로 방문할 수 있는 집의 갯수를 파악해주는 함수
    현재 위치에서 집까지의 거리를 계산 -> idx만큼 더해주기
    :return: 방법이 닿는 집의 최대 수
    """
    maxHome = 0
    nx,ny = n_pos

    #거리 갱신
    dist = {}
    for hx, hy in home :
        d = calDist((nx,ny),(hx,hy)) #해당 집까지의 거리
        if d not in dist :
            dist[d] = 1
        else :
            dist[d] += 1

    #계산
    keys = sorted(list(dist.keys()))
    cnt = 0
    for d in keys :
        cnt += dist[d] #거리가 d인 곳 까지 집의 갯수
        money = getMoney(cnt,d + 1 )
        if money < 0 : continue
        maxHome = max(maxHome , cnt) #거리가 늘어나고도 비용이 손해가 아니면 무조건 갱신될 것

    return maxHome


T = int(input())
for t in range(1,T + 1) :
    n,m = map(int, input().split())
    graph = [list(map(int,input().split())) for _ in range(n) ]

    # 집 위치 탐색
    home = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                home.append((i, j))

    answer = 0
    for i in range(n):
        for j in range(n):
            answer = max(answer, getMaxHome((i, j)))

    print("#{} {}".format(t, answer))