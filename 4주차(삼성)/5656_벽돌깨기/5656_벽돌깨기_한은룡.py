"""
유형 : dfs + bfs

풀이방법
-


"""


from copy import deepcopy
from collections import deque

def dfs(num,numBreak,blocks):
    """
    모든 경우의수를 탐색하고 최대로 깰 수 있는 벽돌의 수를 갱신하는 함수
    :param num: 구슬을 던진 회차? 쵯수?
    :param numBreak: 현재까지 깬 벽돌 수
    :param blocks: 현재 블록 판
    :return: max breaked block
    """
    global maxCount

    if num == n :
        maxCount = max(maxCount , numBreak)
        return

    nextNodeLst = getNextNode(blocks) #현재 상황에서 갈 수 있는 곳

    for node in nextNodeLst :
        curBlocks = deepcopy(blocks) #현재 상황을 우선 저장..

        result = bfs(node,curBlocks) #벽돌을 몇 개 깼는지 저장
        sortBlock(curBlocks)

        if numBreak + result == totalBlocks : #회차가 끝나기전에 이미 다 깼다면 종료
            maxCount = totalBlocks
            return
        dfs(num +1 , numBreak + result,curBlocks)


def getNextNode(blocks):
    """다음 갈 수 있는 노드를 찾는 함수
    :return: list(next node)
    """
    nextNodeLst = []
    for i in range(w): #열
        for j in range(h) : #행
            if blocks[j][i] > 0 :
                nextNodeLst.append((j,i))
                break
        if blocks[j][i] > 0: continue
    return nextNodeLst

dr = [1,-1,0,0] #현재랑 아래로만 이동함..
dc = [0,0,1,-1] #좌우로는 이동함
def bfs(node,blocks):
    """ node에 공이 떨어졌을 때 벽돌을 깨는 함수
    :return: 깬 갯수, 깨지고난 그래프
    """
    r,c = node
    q = deque()
    q.append((r,c,blocks[r][c]))
    cnt = 1 #자기 자신
    blocks[r][c] = 0

    while q :
        r,c,length = q.popleft()
        for i in range(4) :
            for l in range(length):
                nr,nc =r + dr[i] * l  , c + dc[i] * l
                if nr < 0 or nr >= h or nc < 0 or nc >= w : continue
                if blocks[nr][nc] == 1 :
                    cnt += 1
                    blocks[nr][nc] = 0
                elif blocks[nr][nc] > 1 : #지우려는 블럭이 1보다 크면 넘기기기
                    cnt += 1
                    q.append((nr,nc,blocks[nr][nc]))
                    blocks[nr][nc] = 0
                else :pass
    return cnt

def sortBlock(blocks):
    """벽돌이 깨지고난 후 중력을 작용하는 함수
    :return: 깨지고난 후 정렬된 블록
    """
    for i in range(w):
        stack = [] #선입 후 출
        for j in range(h):
            if blocks[j][i] > 0 :
                stack.append(blocks[j][i])
                blocks[j][i] = 0
            else : continue

        for j in range(h-1,-1,-1):
            if stack == list(): break
            blocks[j][i] = stack.pop()


T = int(input())

for t in range(1,T+1):
    n, w, h = map(int, input().split())
    blocks = [list(map(int,input().split())) for _ in range(h)]
    #blocks = []
    #for info in input().split("\n"):
    #    blocks.append(list(map(int,info.split())))

    totalBlocks =0
    for i in range(w):
        for j in range(h):
            if blocks[j][i] != 0 :
                totalBlocks += 1

    maxCount = 0

    dfs(0,0,blocks)
    print('#{} {}'.format(t, totalBlocks - maxCount))


