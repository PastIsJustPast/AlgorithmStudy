C, N = map(int, input().split())
cost2client = {}
for _ in range(N):
    cost, client = map(int, input().split())
    if cost in cost2client:
        cost2client[cost] = max(cost2client[cost], client)
    else:
        cost2client[cost] = client

costs = list(cost2client.keys())
max_cost = 10 ** 6
dp = [0 for _ in range(max_cost)]
for i in range(max_cost):
    for cost in costs:
        if i - cost < 0:
            continue
        dp[i] = max(dp[i - cost] + cost2client[cost], dp[i])
        if dp[i] >= C:
            print(i)
            exit(0)