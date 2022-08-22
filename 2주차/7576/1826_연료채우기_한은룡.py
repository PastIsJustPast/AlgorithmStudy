n = int(input())
oilStation ={}
total = 0
for _ in range(n):
    a,b = map(int,input().split())
    oilStation[a] =b
    total += b

l,p = map(int,input().split())

dist,oil = 0,p  #현재 위치와 남은 기름

def optimize():
    dist, oil = 0, p  # 현재 위치와 남은 기름
    cnt = 0
    if total + p < l : #도착하지 못하면
        return -1

    while True:
        #step
        if oil > l - dist : #바로 종점에 갈 수 있으면 stop
            return cnt

        '''현재 순서에서 들려야할 station 찾기'''
        cnt += 1
        max_oil = 0
        max_station = 0
        for a in oilStation.keys() :
            if dist > a : continue #이미 지나온 곳은 pass
            if a - dist < oil : #현재 오일로 갈 수 있는 위치까지만 탐색하고 가장 기름이 많은 곳으로 간다.
                if max_oil < oilStation[a] :
                    max_station = a
                    max_oil = oilStation[a]

            else : break #현재 오일로 못가면 그냥 멈추기

        dist = oil #갖고 있던 oil로 올 수 있던 곳
        oil = max_oil #도중에 들린 주유소에서 받은 기름 양






d