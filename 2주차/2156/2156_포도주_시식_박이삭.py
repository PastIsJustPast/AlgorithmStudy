"""
Python3
메모리 30840KB
시간 476ms
"""
wines = [int(input()) for _ in range(int(input()))]
dp = [0 for _ in wines]
dp[0] = wines[0]

for i in range(len(wines)):
    if i >= 3:
        dp[i] = max(dp[i - 1], dp[i - 2] + wines[i], dp[i - 3] + wines[i - 1] + wines[i])
    elif i == 2:
        dp[i] = max(wines[0] + wines[1], wines[0] + wines[2], wines[1] + wines[2])
    elif i == 1:
        dp[i] = wines[0] + wines[1]

print(dp[-1])

