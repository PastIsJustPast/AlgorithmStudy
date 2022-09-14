from collections import deque
def bfs(n, info):
    result = []
    q = deque([(0, [0]*len(info))])
    largest = 0
    while q:
        cur, arr = q.popleft()
        # 화살 오버
        if sum(arr) > n:
            continue
        # 다 쏨
        elif sum(arr) == n:
            apeach, ryan = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arr[i] == 0):
                    if info[i] >= arr[i]:
                        apeach += 10 - i
                    else:
                        ryan += 10 - i
            if ryan > apeach:
                dif = ryan - apeach
                if largest > dif:
                    continue
                # 최댓값 갱신
                if largest < dif:
                    largest = dif
                    result.clear() # 리스트 내 모든 요소 제거
                result.append(arr)

        elif cur == 10:
            tmp = arr
            tmp[cur] = n - sum(tmp)
            q.append((-1, tmp))

        # 빼먹었던 부분
        # 이기는 경우 1) 라이언이 어피치보다 1발 더 쏠 경우, 2) 아예 쏘지 않고 화살 세이브
        else:
            tmp = arr
            tmp[cur] = info[cur]+1
            q.append((cur+1, tmp)) # 라이언이 어피치보다 1발 더 쏨

            tmp2 = arr.copy()
            tmp2[cur] = 0
            q.append((cur+1, tmp2)) # 쏘지 않는다.
    return result

def solution(n, info):
    answer = bfs(n, info)
    if not answer:
        return [-1]
    elif len(answer) == 1:
        return answer[0]
    else:
        return answer[-1]