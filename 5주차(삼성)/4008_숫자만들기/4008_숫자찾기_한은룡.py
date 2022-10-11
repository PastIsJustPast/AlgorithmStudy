"""
마지막 테스트 케이스에서 시간초과..
백트래킹으로 풀었음

numOfOperator를 연산자 list로 싹 풀어서 순열문제로 만듦..
아마 똑같은 수식을 여러번 계산하는게 있었던 것 같음..

"""

import math

def permutation(depth): #중복 순열
    global min_value,max_value, cal
    if depth == len(operator) : #n개를 모두 뽑았으면 종료
        value = calculator(numbers,cal)
        min_value = min(min_value,value)
        max_value = max(max_value,value)
        return

    for i in operator : #백트래킹에서 탐색할 노드들
        if visited[i] == False: #전체 횟수를 초과하지 않았다면
            cal.append(operator[i])
            visited[i]  = True
            permutation(depth + 1)

            cal.pop()
            visited[i] = False


def calculator(numbers, cal) :
    result = numbers[0]
    for i in range(len(cal)):
        if cal[i] == 0 : #+
            result += numbers[i+1]
        elif cal[i] == 1 : # -
            result -= numbers[i+1]
        elif  cal[i] == 2 : # *
            result *= numbers[i+1]
        else :
            result /= numbers[i+1]
            if result < 0 :
                result =math.ceil(result)
            else :
                result = math.floor(result)
    return result


T = int(input())
for t in range(1,T+1):
    n = int(input())
    numOfOperators = list(map(int,input().split())) # + - * /
    numbers = list(map(int,input().split()))

    operator = [] # + + - /
    for idx in  range(len(numOfOperators)) :
        i = numOfOperators[idx]
        for _ in range(i) :
            operator.append(idx)

    visited = [False for _ in range(len(operator))]
    cal = []
    min_value = 1e9
    max_value = 0

    permutation(0)

    print(max_value - min_value)
