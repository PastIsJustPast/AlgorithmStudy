from itertools import combinations


def get_taste(taste_map, selected):
    taste = 0
    for r, c in combinations(selected, 2):
        taste += taste_map[r][c] + taste_map[c][r]
    return taste


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    set_N = set(range(N))
    differ = 28 * 40000
    taste_map = [[int(taste) for taste in input().split()] for _ in range(N)]

    for selected in combinations(range(N), N//2):
        comp_sel = set_N - set(selected)
        differ = min(differ, abs(get_taste(taste_map, selected) - get_taste(taste_map, comp_sel)))

    print(f"#{test_case} {differ}")