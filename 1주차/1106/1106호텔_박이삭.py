"""
C : 목표 인원
N : 도시 개수
공백을 기준으로 한 비용과 광고효과 숫자 쌍이 N줄의 입력으로 주어진다.
"""
import sys

input = sys.stdin.readline

C, N = map(int, input().split())

# 목표 인원을 행으로 N개의 도시에 대한 입력을 열로 하는 DP용 2차원 배열 생성
DP = [[0] * N] + [[100001 for _ in range(N)] for _ in range(C)]

cost, effect = map(int, input().split())

# 첫번째 입력으로 첫 열을 초기화
for consumer in range(1, C + 1):
    repeat = (consumer - 1) // effect + 1
    DP[consumer][0] = cost * repeat

# 이어서 주어지는 입력들에 따라 이후의 열들을 최적 값으로 update.
for city_idx in range(1, N):
    cost, effect = map(int, input().split())
    for consumer in range(1, C + 1):
        repeat = (consumer - 1) // effect + 1
        DP[consumer][city_idx] = min(
            DP[consumer][city_idx - 1],
            min(
                [
                    DP[max(0, consumer - r * effect)][city_idx] + cost * r
                    for r in range(1, repeat + 1)
                ]
            ),
        )

print(DP[C][N - 1])
