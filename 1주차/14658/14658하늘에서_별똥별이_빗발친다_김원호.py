N, M, L, K = map(int, input().split())

points = []
cols = set()
rows = set()
for _ in range(K):
    x, y = map(int, input().split())
    points.append((x, y))
    cols |= set([x])
    rows |= set([y])

max_reflect = 0
for tx in cols:
    for ty in rows:
        reflect = 0
        for px, py in points:
            if 0 <= tx - px <= L and 0 <= ty - py <= L:
                reflect += 1
        if reflect > max_reflect:
            max_reflect = reflect

print(K - max_reflect)