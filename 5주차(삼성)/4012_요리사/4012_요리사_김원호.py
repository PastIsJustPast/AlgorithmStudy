import sys


sys.stdin = open('../../../ArgorithmStudy/5주차(삼성)/4012_요리사/sample_input.txt')


from itertools import combinations


def get_taste(comb):
    taste = 0
    for elt1 in comb:
        for elt2 in comb:
            taste += synergy[elt1][elt2]
    return taste


T = int(input())
for t in range(1, T+1):
    N = int(input())
    synergy = [[int(x) for x in input().split()] for _ in range(N)]
    combs = combinations(range(1, N), N // 2)
    answer = 10 ** 10
    for comb in combs:
        taste1 = get_taste(comb)
        taste2 = get_taste(set(range(N)) - set(comb))
        answer = min(answer, abs(taste1 - taste2))
    print(f'#{t} {answer}')