# time : 1.5342907905578613
n = int(input())
li = [int(input()) for _ in range(n)]
li.insert(0, 0)
dp = [0]
dp.append(li[1])

if n >= 2:
    dp.append(li[1] + li[2])
'''
dp[0] = 0
dp[1] = 6
dp[2] = 6+10
dp[3] = max(6+10, 6+13, 10+13) = 23
dp[4] = max(6+10+9, 6+13+9, 10+13)
'''
for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-2] + li[i], dp[i-3] + li[i-1] + li[i]))
print(dp[n])