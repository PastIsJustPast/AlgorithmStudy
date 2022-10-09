# 처음에 잘못 생각한 부분 : nC2 경우 구해서 각 경우의 수별로 합 구함
from itertools import combinations

def synergy(s, pick):
    res = 0
    for i, j in combinations(pick, 2):
        res += s[i][j] + s[j][i]
    return res

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    A, B = 0, 0
    min_value = 2e9
    '''
    A를 선택하는 경우 : 0 ~ n 중 n//2만큼 조합
    B를 선택하는 경우 : 전체 경우 - A
    '''
    for i in combinations(range(n), n//2): # 그냥 n쓰면 int object is not iterable
        A = synergy(s, i)
        B = synergy(s, list(set(range(n)) - set(i)))
        if min_value > abs(A-B):
            min_value = abs(A-B)
    print("#{} {}".format(tc, min_value))