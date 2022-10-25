'''
        메모리(kb) 시간(ms)
python3 30852    5292
pypy3   118520   276
'''


def get_dp_line(i):
    global dp_x, dp_y
    tmp_dp_x = dp_x.copy()
    tmp_dp_y = dp_y.copy()
    tmp_dp_x[i-1] = dp_y[i]
    tmp_dp_y[i-1] = dp_x[i]
    for j in range(i, len(X) + 1):
        if X[j - 1] == Y[i - 1]:
            tmp_dp_x[j] = dp_x[j - 1] + A
        else:
            tmp_dp_x[j] = max(B + tmp_dp_x[j - 1],
                              B + dp_x[j],
                              C + dp_x[j - 1])
    for j in range(i, len(Y) + 1):
        if X[i - 1] == Y[j - 1]:
            tmp_dp_y[j] = dp_y[j - 1] + A
        else:
            tmp_dp_y[j] = max(B + tmp_dp_y[j - 1],
                              B + dp_y[j],
                              C + dp_y[j - 1])
    dp_x = tmp_dp_x
    dp_y = tmp_dp_y


A, B, C = map(int, input().split())
X = input()
Y = input()
m = min(len(X), len(Y))
dp_x = [0 for _ in range(len(X) + 1)]
dp_y = [0 for _ in range(len(Y) + 1)]
for i in range(len(X) + 1):
    dp_x[i] = B * i
for i in range(len(Y) + 1):
    dp_y[i] = B * i

for i in range(1, m + 1):
    get_dp_line(i)
if len(X) > len(Y):
    print(dp_x[-1])
else:
    print(dp_y[-1])
