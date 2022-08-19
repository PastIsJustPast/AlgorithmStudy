#kb     ms      lang
#32908	88  	Python 3
import heapq, sys
input = sys.stdin.readline
n = int(input())

#주유소 위치, 연료량
gas = [tuple(map(int, input().split())) for _ in range(n)]

#목적지 거리, 보유 연료량
l, p = map(int, input().split())

#주유소 위치에 목적지 정보 끼워넣기
gas = sorted((gas + [(l, 0)]), key=lambda x : x[0])

#현재 위치, 방문 count
now, cnt = 0, 0

past = []
for i in range(n+1):
    #보유 연료보다 다음 목적지까지 기름이 더 필요한 경우 반복
    while p < gas[i][0] - now:
        #더이상 기름 넣을 주유소가 없으면 종료
        if not past :
            print(-1)
            exit(0)

        p -= heapq.heappop(past)
        cnt += 1
    
    heapq.heappush(past, -gas[i][1])
    p = p - (gas[i][0] - now)    # 기름 소비
    now = gas[i][0]         # 위치 이동
    
    if now == l : break

print(cnt)
