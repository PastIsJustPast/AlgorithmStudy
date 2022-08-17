c, n = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
_max = 2147000000

dp = [0] + [_max] * (c + 100) # dp[0] = 0
for cost, customer in li:
    for pos in range(customer, c+101):
        # 초깃값은 max로 설정 -> 최소 비용 필요
        # 현재 n명 고객 유치 비용 = min(현재 n명 고객 유치 비용, 유치 가능 인원 비용 + 인원 유치 비용)
        dp[pos] = min(dp[pos], dp[pos - customer] + cost)
print(min(dp[c:c+101])) # 투자할 돈의 최솟값
