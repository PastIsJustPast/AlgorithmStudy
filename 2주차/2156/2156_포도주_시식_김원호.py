# python3 31860 KB, 464 ms
# pypy3 116872 KB, 144 ms

n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0][1] = wines[0]
for i in range(1, n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + wines[i]
    dp[i][2] = dp[i-1][1] + wines[i]
print(max(dp[-1]))