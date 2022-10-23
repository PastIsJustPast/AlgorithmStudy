'''
        메모리(kb) 시간(ms)
python3 30840    3692
pypy3   150744   2596
'''

def dfs(n, x, y, visit, prob):
    if n == 0:
        return prob
    dfs_rets = []
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (nx, ny) not in visit:
            visit.add((nx, ny))
            ret = dfs(n-1, nx, ny, visit, prob * probabilities[k] / 100)
            visit.remove((nx, ny))
            dfs_rets.append(ret)
    return sum(dfs_rets)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, *probabilities = map(int, input().split())
visit = set()
visit.add((0, 0))
answer = dfs(N, 0, 0, visit, 1)
print(answer)
