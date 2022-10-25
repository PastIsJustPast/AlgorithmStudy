'''
        메모리(kb) 시간(ms)
python3 ??       시간초과
pypy3   154552   3016
'''


def get_dp_line(i):
    global dp
    for j in range(i, len(X) + 1):
        if X[j-1] == Y[i-1]:
            dp[(j, i)] = dp[(j-1, i-1)] + A
        else:
            dp[(j, i)] = max(B + dp[(j-1, i)],
                             B + dp[(j, i-1)],
                             C + dp[(j-1, i-1)])
    for j in range(i, len(Y) + 1):
        if X[i-1] == Y[j-1]:
            dp[(i, j)] = dp[(i - 1, j - 1)] + A
        else:
            dp[(i, j)] = max(B + dp[(i-1, j)],
                             B + dp[(i, j-1)],
                             C + dp[(i-1, j-1)])
    for j in range(i-1, n):
        dp.pop((i-1, j), None)
        dp.pop((j, i-1), None)


A, B, C = map(int, input().split())
X = input()
Y = input()
n = max(len(X), len(Y))
m = min(len(X), len(Y))
dp = {}
for i in range(n + 1):
    dp[(i, 0)] = B * i
    dp[(0, i)] = B * i

for i in range(1, m + 1):
    get_dp_line(i)
print(dp[(len(X), len(Y))])
