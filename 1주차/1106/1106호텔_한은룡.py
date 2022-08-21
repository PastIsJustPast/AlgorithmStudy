'''
유형 : dp
풀이방법 :
i번째 인원을 모으기 위한 최소비용을 각 단계마다 수행해주는 dp문제
i번째 인원을 모으기 위한 최소비용은 (i - 광고 효과)번쨰 인원을 모으기 위한 최소비용에 광고 비용을 더한 값들 중 최소값이다.

'''


c,n = map(int,input().split())
hotel = [] #첫 원소 : 비용, 두번째 원소 : 고객의 수
'''
for info in input().split("\n"):
    hotel.append(list(map(int,info.split())))
'''
for _ in range(n):
    hotel.append(list(map(int,input().split())))

#dp테이블 생성. index명까지 모으는데 드는 최소 비용
dp = [0] * (c+1)

#d(i)은 d(i-hotel[:][1]) + hotel[:][0] 의 최소값

for idx in range(1,c+1):
    sub = []
    for cost, effect in hotel :
        if idx < effect :  #idx명이 cost를 지불했을 때 효과인 effect명보다 작다면
            sub.append(cost)
        else :
            sub.append(dp[idx - effect]  + cost)

    dp[idx] = min(sub) #현재 가능한 값 중에서 가장 최소비용

print(dp[c])