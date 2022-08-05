"""
N, M : 별똥별이 떨어지는 구역의 가로, 세로 길이
L : 정사각형 트램펄린 한 변의 길이
K : 별똥별의 수
"""
import sys

from collections import defaultdict

input = sys.stdin.readline

N, M, L, K = map(int, input().split())

# 사용할 storage 생성
r_stars = defaultdict(set)
c_stars = defaultdict(set)
final_stars = K

# 주어지는 별똥별 좌표를 행과 열에 따라 storage에 각각 추가
for _ in range(K):
    r, c = map(int, input().split())
    r_stars[r].add((r, c))
    c_stars[c].add((r, c))

r_keys = sorted(r_stars.keys())
c_keys = sorted(c_stars.keys())

# 특정 행을 기준으로 트램펄린이 놓였을 각각의 경우의 별똥별 좌표 합집합
r_unions = {}
for i, r in enumerate(r_keys):
    r_union = None
    for rn in r_keys[i:]:
        if rn <= r + L:
            if r_union:
                r_union |= r_stars[rn]
            else:
                r_union = r_stars[rn]
        else:
            break
    if r_union is not None:
        r_unions[r] = r_union

# 특정 열을 기준으로 트램펄린이 놓였을 각각의 경우의 별똥별 좌표 합집합
c_unions = {}
for i, c in enumerate(c_keys):
    c_union = None
    for cn in c_keys[i:]:
        if cn <= c + L:
            if c_union:
                c_union |= c_stars[cn]
            else:
                c_union = c_stars[cn]
        else:
            break
    if c_union is not None:
        c_unions[c] = c_union

# 가능한 열과 행에 따라 행 기준 좌표들과 열 기준 좌표들의 교집합에 따른 최솟값을 구한다.
for r in sorted(r_unions.keys()):
    for c in sorted(c_unions.keys()):
        final_stars = min(K - len(r_unions[r] & c_unions[c]), final_stars)

print(final_stars)
