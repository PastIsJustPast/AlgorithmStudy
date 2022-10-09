def synergy(johab):  # 음식의 시너지값 계산 함수
    score = 0
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            score += recipe[johab[i]][johab[j]] + recipe[johab[j]][johab[i]]
    return score


def dfs(idx, k):
    global result
    if idx == N // 2:  # 한 음식에 선택되는 재료개수 = N // 2 이므로 재료개수만큼 탐색
        A = []  # A 음식에 들어갈 재료
        B = []  # B 음식에 들어갈 재료
        for j in range(N):  # 방문 배열 개수만큼 탐색해서
            if visit[j]:  # 방문 내역이 있다면 A로 아니면 B에 저장
                A.append(j)
            else:
                B.append(j)
        recipe_A = synergy(A)
        recipe_B = synergy(B)
        if abs(recipe_A - recipe_B) < result:
            result = abs(recipe_A - recipe_B)
        return

    for i in range(k, N):  # 조합 k 인자 i까지 봤으면 다음번에는 앞에 탐색했던 부분 볼 필요 없음 k인자 없으면 0부터 탐색하기에 순열이 되버림
        if not visit[i]:
            visit[i] = 1
            dfs(idx + 1, i + 1)
            visit[i] = 0


T = int(input())
for t in range(T):
    N = int(input())
    visit = [0 for _ in range(N)]
    recipe = [list(map(int, input().split())) for _ in range(N)]
    result = 99999999999

    dfs(0, 0)
    print('#{} {}'.format(t + 1, result))