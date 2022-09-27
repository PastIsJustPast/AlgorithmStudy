from copy import deepcopy

dy = [0,-1,0,1,0] #정지, 상, 우 하 좌
dx = [0,0,1,0,-1]
def moveRoute(start,direction):
    """초와 이동 경로에 따라 초별 배터리 장소를 찾는 함수
    :return: 초별 위치
    """
    answer = []
    y, x = start
    answer.append(battery[y][x])

    for d in direction:
        y,x = y + dy[d], x + dx[d]
        answer.append(battery[y][x])

    return answer


def getMaxCharge(t,A,B):
    answer = 0

    if A[t] == list() and B[t] == list() : # 둘다 빈칸일 경우
        answer = 0
        return answer
    elif A[t] == list() or B[t] == list() : #둘 중 하나만 빈칸일 경우
        if A[t] != list() : #A만 있을 때
            answer = A[t][0][0]
            return answer
        else :
            B[t] != list() #B만 있을 때
            answer = B[t][0][0]
            return answer
    else : #둘 다 배터리 위에 있을 경우
        if A[t][0][1] == B[t][0][1] : #같은 배터리 위에 있을 경우
            answer = A[t][0][0] #우선 제일 큰값 넣고
            if len(A[t]) >1 and len(B[t]) > 1 : #둘다 2개 이상 있는 경우
                answer += max(A[t][1][0],B[t][1][0]) # 두번째 값을 비교하여 큰 값 추가
            elif len(A[t]) > 1 and  len(B[t]) == 1 : #A만 두개 이상일 경우
                answer += A[t][1][0]
            elif len(A[t]) ==1 and len(B[t]) > 1 : #B만 두개 이상일 경우
                answer += B[t][1][0]
            else : #둘다 1개밖에 없는 경우는 이미 넣었으니 패스
                pass
            return answer
        else :  #둘다 배터리 위이지만 서로 다른 배터리 위에 있을 경우
            answer = A[t][0][0] + B[t][0][0]
            return answer


T = int(input())
for testNum in range(1,T+1):
    m, a = map(int, input().split())
    route = [list(map(int,input().split())) for _ in range(2)]

    #for info in input().split("\n"):
    #    route.append(list(map(int, info.split())))

    # 배터리 맵 설정
    battery = [[[] for _ in range(11)] for _ in range(11)]  # 배터리 위치, 2차원 리스트의 원소가 리스트
    num = 1  # 배터리 번호
    #for info in input().split("\n"):
    for _ in range(a):
        x, y, c, p = map(int, input().split())
        for i in range(-c, c + 1):  # 거리
            for j in range(-c, c + 1):
                ny, nx = y + i, x + j
                if ny <= 0 or ny > 10 or nx <= 0 or nx > 10: continue
                if abs(ny - y) + abs(nx - x) > c: continue
                battery[ny][nx].append((p, num))  # 크기순 정렬 편하게 하려구 p, num순
        num += 1

    # 배터리 크기순 정렬
    for i in range(1, 11):
        for j in range(1, 11):
            if len(battery[i][j]) > 1:  # 2개 이상 있다면 정렬
                battery[i][j] = sorted(battery[i][j], reverse=True)

    A = moveRoute((1, 1), route[0])
    B = moveRoute((10, 10), route[1])

    result = 0
    for t in range(len(A)):
        result += getMaxCharge(t, A, B)

    print('#{} {}'.format(testNum, result))


