"""
pypy3     python
130632kb   30840kb
 1272ms    4736ms

유형 : DFS + 재귀
풀이방법
- 좌표랑 상관없이 한번 로봇이 간곳만 체크해서 되돌아가지 않으면 성공
- 모든 가능한 경로중에 성공한 경우를 찾아서 확률로 계산하면 됨

"""


n, E, W, S, N = map(int, input().split())
probability = [E, W, S, N]
answer = 0

direc = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 4방향 탐색

def dfs(r, c, visited, total):
    global answer
    #종료조건
    if len(visited) == n+1:
        answer += total
        return

    for i in range(4) :
        nr = r + direc[i][0]
        nc = c + direc[i][1]
        if (nr, nc) not in visited:
            visited.append((nr, nc)) #추가
            dfs(nr, nc, visited, total*probability[i])
            visited.pop() #제거


dfs(0, 0, [(0, 0)], 1)
print(answer * (0.01 ** n))