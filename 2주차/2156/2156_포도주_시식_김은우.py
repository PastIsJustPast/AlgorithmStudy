#kb     ms  lang
#30840	76	Python 3
import sys
input = sys.stdin.readline
n = int(input())

arr = [0] + [int(input()) for _ in range(n)]
dp = [0 for _ in range(n+1)]

if n < 3 :
    print(sum(arr))
    exit()

dp[1] = arr[1]
dp[2] = arr[1]+arr[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-3]+arr[i]+arr[i-1],
                dp[i-2]+arr[i],
                dp[i-1])

print(dp[-1])