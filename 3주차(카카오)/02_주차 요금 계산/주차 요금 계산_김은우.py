import math
from collections import defaultdict
def solution(fees, records):
    '''
    fees
    0. 기본시간
    1. 기본요금
    2. 단위시간
    3. 단위요금

    모든 내역을 dictionary에 저장
    내역이 길이가 홀수라면 23:59 추가

    모든 내역을 짝수번 입력 받았으므로
    n//2 번 in & out 시간을 계산하여 저장
    '''

    #입출차 내역 저장
    dic = defaultdict(list)
    for record in records : 
        time, num, _ = record.split()
        a, b = time.split(':')
        time = int(a) * 60 + int(b)
        
        dic[num].append(time)

    #나간 내역이 없는 차는 23:59 출차로 저장
    for x in dic.keys():
        if len(dic[x]) % 2 == 1 :
            dic[x].append(1439)

    #머무른 시간 저장
    answer = []
    for x in sorted(dic.keys()):
        t = 0
        for y in range(0, len(dic[x]), 2):
            t += dic[x][y+1] - dic[x][y] 
        
        #요금 계산
        t -= fees[0]
        charge = fees[1]

        if t >= 0 :
            charge += math.ceil(t/fees[2]) * fees[3]
        answer.append(charge)

    return answer