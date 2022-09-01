# time : 1.7793426513671875
n, m, h = map(int, input().split())
cord = [list(map(int, input().split())) for _ in range(n)]
x, y = 0, 0
mincho = []

'''
시간 초과
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
'''

def dfs(rx, ry, hp, milk):
    global res
    for x, y in mincho:
        if cord[x][y] == 2:
            distance = abs(rx - x) + abs(ry - y)
            # 체력이 남아있다면 이동하고 해당 위치 0으로 바꿈
            if distance <= hp:
                cord[x][y] = 0
                dfs(x, y, hp+h-distance, milk+1)
                cord[x][y] = 2
    if abs(rx-x) + abs(ry-y) <= hp:
        res = max(res, milk)

for i in range(n):
    for j in range(n):
        if cord[i][j] == 2:
            mincho.append([i, j]) # 우유 위치
        if cord[i][j] == 1:
            x, y = i, j # 집 위치
res = 0
dfs(x, y, m, 0)
print(res)

'''
10 2 3
0 0 0 0 0 0 0 0 0 0
0 0 0 2 0 0 0 0 0 0
0 2 0 0 0 0 2 0 0 0
0 0 0 0 0 0 0 0 0 0
0 2 0 0 2 0 0 0 0 0
0 0 0 0 0 0 0 0 2 0
0 0 0 1 0 0 2 0 0 0
0 0 0 0 2 0 0 0 0 0
0 2 0 0 0 0 0 0 0 0
0 0 0 0 0 2 0 0 0 0
'''