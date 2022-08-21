# python3 30840 KB, 708 ms
# pypy3 166356 KB, 2228 ms

def dfs(x, y, health, choco_milks):
    global max_choco_count
    if abs(sx - x) + abs(sy - y) <= health:
        max_choco_count = max(max_choco_count, total_choco_milks_count - len(choco_milks))
    if max_choco_count == total_choco_milks_count:
        return
    choco_milks = choco_milks.copy()
    for i, choco_milk in enumerate(choco_milks):
        nx, ny = choco_milk
        dist = abs(nx - x) + abs(ny - y)
        if health >= dist:
            next_choco_milks = choco_milks[:i] + choco_milks[i+1:]
            dfs(nx, ny, health - dist + H, next_choco_milks)


N, M, H = map(int, input().split())
MAP = []
choco_milks = []
for i in range(N):
    row = list(map(int, input().split()))
    for j, elt in enumerate(row):
        if elt == 2:
            choco_milks.append((i, j))
        elif elt == 1:
            sx, sy = (i, j)

total_choco_milks_count = len(choco_milks)
max_choco_count = 0
dfs(sx, sy, M, choco_milks)
print(max_choco_count)
