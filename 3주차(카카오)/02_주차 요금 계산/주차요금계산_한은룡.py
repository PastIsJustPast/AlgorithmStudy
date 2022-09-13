'''
문제 유형 : 단순 구현? 그리디?

풀이 방법
 - records를 살펴서 차량의 누적 이용시간을 계산
    - 차량번호별 입차시간, 차량번호별 현재 주차여부, 차량번호별 누적 이용시간을 모두 dict로 관리
    - 모든 records를 살핀 후에 주차상태가 입차상태라면 출차시간을 23:59로 간주하고 다시 계산
 - 누적 이용시간을 누적 이용금액으로 환산

쟁점
- 틀리지 않고 푸는게 제일 중요한듯!
'''


import math

def diff_time(b, f):
    '''
    두 시각의 차이를 분단위로 출력하는 함수
    '''
    b = list(map(int, b.split(":")))
    f = list(map(int, f.split(":")))
    if b[1] > f[1]:
        return (f[0] - b[0] - 1) * 60 + 60 - (b[1] - f[1])
    else:
        return (f[0] - b[0]) * 60 + f[1] - b[1]


def price(t, fees):
    '''
    주차장에 머무른 누적 시간 t의 요금을 출력하는 함수
    '''
    if t <= fees[0]:  # 기본 시간 미만
        return fees[1]
    else:
        t -= fees[0]  # 기본 시간 초과
        return math.ceil(t / fees[2]) * fees[3] + fees[1]


def solution(fees, records):
    answer = []
    name = {}  # 입차시간 기록
    parking = {}  # 차량의 현재 주차여부
    time = {}  # 하루종일 주차장에 머무른 시간

    for info in records:
        a, b, c = info.split()
        time[b] = 0

    '''누적 이용시간 계산'''
    # 1. 입차와 출차기록이 있는 차량
    for info in records:
        a, b, c = info.split()
        if b not in parking or parking[b] == "OUT":  # 여태 방문한적이 없거나 밖에 있다면 이번 내역은 무조건in임
            parking[b] = c  # 입차처리
            name[b] = a
        elif parking[b] == "IN":  # 이미 차가 있다는건 이번 내역은 out임
            parking[b] = c  # 출차처리
            time[b] += diff_time(name[b], a)
            name[b] = 0  # 입차착 시간 초기화

    # 2. 방문했는데 안나간 차량
    for i in time:
        if parking[i] == "IN":
            time[i] += diff_time(name[i], "23:59")

    '''누적 요금 계싼'''
    result = []
    for i in time:
        result.append((i, price(time[i], fees)))  # 차번호와 요금
    result.sort()  # 차번호대로 정렬

    answer = [x[1] for x in result]
    return answer