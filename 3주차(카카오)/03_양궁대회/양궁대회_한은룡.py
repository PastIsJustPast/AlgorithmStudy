from itertools import combinations_with_replacement

def diff_socore(info,ryan) :
    res1= 0 # 어피치
    res2= 0 # 라이언
    for i in range(11):
        if ryan[i] ==0 and  info[i]== 0 :
            continue
        if ryan[i] > info[i] :
            res2 += (10 - i)
        else :
            res1 += (10 - i)

    if res2 > res1 : return res2 - res1# 승리시
    else : return 0

def make_ryan(temp):  #temp는 1부터 10까지 랜덤한n개
    result = [0] * 11
    for i in range(len(temp)) : #n개의 화살 1
        result[10-temp[i]] += 1
    return result


def solution(n,info):
    answer =0
    max_score = 0
    for temp in combinations_with_replacement(range(0,11),n):
        ryan=make_ryan(temp) #과녁 정보 생성
        if max_score < diff_socore(info,ryan) :
            max_score = diff_socore(info,ryan)
            answer = ryan
    if answer == 0 :
        return [-1]
    return answer