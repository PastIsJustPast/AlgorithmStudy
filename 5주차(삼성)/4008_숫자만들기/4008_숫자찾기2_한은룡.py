"""
+(1) , +(2), - , / 가 있을 경우 
+(1) 과 +(2)의 순서는 상관 없음

즉 뽑는 순서에서 +가 오는게 중요하지 몇 번째 +가 오는지는 중요하지 않음

즉, 단순 순열로 구현하는게 아니라 각 연산자가 몇 번 뽑혔는지 계산하는 조합 문제로 구현해야함

"""

import math
from copy import deepcopy

def permutation(depth): #중복 순열
    global min_value,max_value, cal
    if depth == n-1 : #n개의 연산자를 뽑으면 끝
        value = calculator(numbers,cal)
        min_value = min(min_value,value)
        max_value = max(max_value,value)
        return

    for i in range(4) : #백트래킹에서 탐색할 노드들
        if visited[i] > 0 : #아직 뽑을 수 있는 수량이 남았으면
            visited[i] -= 1
            cal.append(i)
            permutation(depth + 1)

            cal.pop()
            visited[i] += 1


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
    numbers = list(map(int, input().split()))

    visited = deepcopy(numOfOperators)
    cal = []
    min_value = 1e9
    max_value = -1e9

    permutation(0)

    print(max_value - min_value)
