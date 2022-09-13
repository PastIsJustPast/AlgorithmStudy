def solution(n, info):
    def get_diff(arrows):
        ryan_score = 0
        apeach_score = 0
        for i in range(10):
            if arrows[i] != 0:
                ryan_score += 10 - i
            elif info[i]:
                apeach_score += 10 - i
        return ryan_score - apeach_score

    def dfs(arrows, index):
        nonlocal max_diff, answer
        if sum(arrows) > n:
            return
        if index == 10:
            diff = get_diff(arrows)
            arrows += [n - sum(arrows)]
            if diff > max_diff:
                max_diff = diff
                answer = arrows
            elif diff == max_diff:
                for i in range(10, -1, -1):
                    if arrows[i] > answer[i]:
                        answer = arrows
                        return
                    elif arrows[i] < answer[i]:
                        return
            return
        dfs(arrows + [0], index + 1)
        dfs(arrows + [info[index] + 1], index + 1)

    max_diff = 0
    answer = [0] * 11
    dfs([], 0)
    if max_diff == 0:
        return [-1]
    return answer
