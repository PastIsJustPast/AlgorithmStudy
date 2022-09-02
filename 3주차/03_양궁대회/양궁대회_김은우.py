MAX = 0
answer = []
def dfs(idx, apeach, lion, n):
    lion2 = lion.copy()
    global MAX, answer
    if idx == n :
        a = 0
        l = 0
        for i in range(11):
            if apeach[i] == lion2[i] == 0 :
                continue
            elif apeach[i] < lion2[i] :
                l += i
            else :
                a += i

        if MAX < l - a :
            MAX = l - a
            answer = lion2
        return

    for i in range(11):
        lion2[i] += 1
        dfs(idx+1, apeach, lion2, n)
        lion2[i] -= 1

def solution(n, info):
    dfs(0, info[::-1], [0]*11, n)
    return answer[::-1]