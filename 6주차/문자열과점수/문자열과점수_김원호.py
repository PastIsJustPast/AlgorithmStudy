# 메모리 초과
# 메모리 초과라서 딕셔너리로 바꿨는데도 메모리초과
# 메모리 초과라서 절반정도 지우면서 했더니 시간초과

import sys
import random
sys.setrecursionlimit(10 ** 5)


def get_dp(i, j):
    global dp
    if i < 0 or j < 0:
        return B * (max(i, j) + 1)
    if (i, j) not in dp:
        if X[i] == Y[j]:
            ret = A + get_dp(i - 1, j - 1)
        else:
            a = B + get_dp(i - 1, j)
            b = B + get_dp(i, j - 1)
            c = C + get_dp(i - 1, j - 1)
            ret = max(a, b, c)
        if len(dp) > 800000:
            keys = random.sample(list(dp.keys()), 400000)
            for key in keys:
                del dp[key]
        dp[(i, j)] = ret
    return dp[(i, j)]


A, B, C = map(int, input().split())
D = max(2 * B, C)
X = input()
Y = input()

dp = {}
if X[0] == Y[0]:
    dp[(0, 0)] = A
else:
    dp[(0, 0)] = D

print(get_dp(len(X) - 1, len(Y) - 1))