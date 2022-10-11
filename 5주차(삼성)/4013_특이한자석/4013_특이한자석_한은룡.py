from copy import deepcopy
from collections import deque



def move(num,d) :
    global visited
    if visited[num] == True: return  # 이미 회전했으면 끝내

    for idx, target in connection[num] : #idx와 target[0]target[1]이 똑같으면 됨
        if visited[num] == False : #한번도 안돌았다면
            if gear[num][idx] == gear[target[0]][target[1]] : #같으면 아무 문제 없음
                temp = gear[num]
                temp = rotate(temp,d)
                gear[num] = temp
                visited[num] = True
                return #더이상 같은거 없으면 끝내

            else :
                temp = gear[num]
                temp = rotate(temp, d)
                gear[num] = temp
                visited[num] = True
                move(target[0] , -1 * d )

        else : #한번 돌았다면 옆 톱니와 체크만
            if gear[num][idx] != gear[target[0]][target[1]] :
                move(target[0], -1 * d)

def rotate(q,d):
    if d == 1 : #시계면
        q.appendleft(q.pop())
    else :
        q.append(q.popleft())
    return q

T = int(input())
for t in range(1,T+1):
    k = int(input())
    #graph = [deque(map(int,input().split())) for _ in range(4)]

    graph = []
    for info in input().split("\n"):
        graph.append(deque(map(int,info.split())))
    order = [ list(map(int,input().split())) for _ in range(k)] #1 시계, -1 반시계


    gear = deepcopy(graph)

    connection = {0 : [(2, (1,6) )] , 1 : [(2, (2,6)), (6, (0,2))] , 2 : [(2,(3,6)) , (6, (1,2))] ,3 : [(6, (2,2))] }

    for i in range(k):
        num,d = order[i]
        num -= 1

        visited = [False for _ in range(4)]
        move(num,d)

    answer = 0
    for i in range(4):
        answer += gear[i][0] *(2 ** (i))

    print('#{} {}'.format(t,answer))


