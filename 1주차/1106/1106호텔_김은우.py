INF = 1000*20*100
c, n = map(int, input().split())
dp = [INF for _ in range(c+101)]
dp[0] = 0

info = [tuple(map(int, input().split())) for _ in range(n)]

#비용, 고객
for cost, cust in info:
    for i in range(c+1):
        dp[i] = min(dp[i], dp[max(0, i-cust)]+cost)

print(dp[c])