'''
python3  pypy3
33932kb  118392kb
504ms    284ms

풀이방법
1. 현재 위치에서 갈 수 있는 곳 중 기름을 가장 많이 주는 곳으로 이동 -> 기름 총 합이 목적지까지 간당간당한 경우 틀림
2. 현재 위치에서 갈 수 있는 곳 중 기름을 가장 많이 주는 곳으로 이동 -> 목적지까지 시행 -> 만약 끝까지 못간다면 그다음 가까운 정유소에서 시작

종료 규칙
- 시작하자마자 갖고 있는 oil로 도착할 수 있는 경우
- 총 합으로도 가지 못하는 경우
- 기름이 부족해서 다음 정유소까지 가지 못하는 경우

'''

import heapq

n = int(input())
oilStation = []
for _ in range(n):
    a,b = map(int,input().split())
    heapq.heappush(oilStation, (a, -b))

totalDistance,nowOil = map(int,input().split())


if totalDistance <= nowOil : cnt = 0 #갖고 있는 기름으로 갈 수 있는 경우
else :
    cnt = 0
    oilHeapq = [] #이동한 곳을 나타냄
    nowDistance = 0  #현재 위치

    while True :
        #종료규칙 1번
        if nowDistance + nowOil >= totalDistance : #현재 위치에서 현재 보유한 기름으로 종착지까지 갈 수 있으면
            break

        #갈 수 있는 정유소 탐색
        while oilStation : #더 이상 갈 수 있는 station 이 없으면 종료
            d,o = oilStation[0] #가장 가까운 곳
            if d - nowDistance <= nowOil : #현재 위치에서 현재 기름으로 갈 수 있는 정유소라면 최대 큐에 삽입
                distance, gas = heapq.heappop(oilStation)
                heapq.heappush(oilHeapq , (gas,distance))
            else : #갈 수 있는 곳이 없다
                break

        #갈 수 있는 곳 중 가장 많은 연료를 주는 곳
        if oilHeapq : #갈 수 있는 곳이 있을 경우
            max_gas , d = heapq.heappop(oilHeapq)
            nowOil -= d - nowDistance #그 정유소까지의 거리를 현재 보유하고 있는 oil에서 제거
            nowOil -= max_gas
            nowDistance = d
            cnt += 1

        else : #현재 위치에서 갈 수 있는 정유소가 없는 경우
            if nowDistance + nowOil < totalDistance :
                cnt = -1
                break
print(cnt)