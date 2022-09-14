def solution(n, info):
    dp = [[0 for _ in range(n + 1)] for _ in range(len(info) + 1)]
    path = [[[] for _ in range(n + 1)] for _ in range(len(info) + 1)]
    appeach = 0
    for i, target in enumerate(info):
        appeach += (10 - i) * bool(target)
        for j in range(n + 1):
            if j <= target:
                dp[i + 1][j] = dp[i][j]
                path[i + 1][j] = path[i][j] + [0]
            elif dp[i][j - (target + 1)] + (10 - i) * [1,2][bool(target)] >= dp[i][j]:
                dp[i + 1][j] = dp[i][j - (target + 1)] + (10 - i) * [1,2][bool(target)]
                path[i + 1][j] = path[i][j - (target + 1)] + [target + 1]
            else:
                dp[i + 1][j] = dp[i][j]
                path[i + 1][j] = path[i][j] + [0]

    result = 0
    result_path = None
    for i, value in enumerate(dp[-1]):
        if value - appeach > result:
            result = value - appeach
            result_path = path[-1][i]

    if result_path:
        result_path[-1] += n - sum(result_path)
        return result_path
    else:
        return [-1]
