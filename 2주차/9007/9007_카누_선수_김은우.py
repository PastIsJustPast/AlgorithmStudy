'''
메모리     시간     언어
318600    9652     pypy3
python은 실패

# 문제 푸는 과정
처음엔 4중 for문으로 풀려 했으나 시간초과
학생의 수가 많아 2진탐색으로 하려 했으나 4개의 반을 어떻게 2진탐색 해야 할 지 풀지 못함.
결국 풀지 못하고 풀이를 검색하여 반을 2개씩 더하여 계산한다는 부분을 참고함
기존에 2진 탐색하려던 코드에 적용하여 문제를 해결
"if SUM_1 + SUM_2 == k " 조건문을 넣고자 하였으나 시간초과로 불가능함... 시간초과 아슬하게 통과한듯하다.

# 문제풀이
4개의 반을 2개의 그룹으로 나눠 각각 합 경우의 수를 구함
2 그룹을 2중 for문과 2진탐색을 통해 가장 k에 가까운 합 경우의 수를 구하여 출력
'''
import sys, bisect
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    k, n = map(int, input().split())
    classes = [list(map(int, input().split())) for _ in range(4)]
    
    SUM_1 = set()   #1, 2반 학생들의 합 경우의 수
    SUM_2 = set()   #3, 4반 학생들의 합 경우의 수
    for i in range(n) :
        for j in range(n) :
            SUM_1 |= {classes[0][i] + classes[1][j]}
            SUM_2 |= {classes[2][i] + classes[3][j]}
    
    SUM_1 = list(SUM_1)
    SUM_2 = sorted(list(SUM_2))
    #SUM_2의 길이 저장
    ls = len(SUM_2) - 1
    
    #가장 가까운 근사값
    closest = 1e9
    
    for i in SUM_1:
        #이진 탐색하여 가장 k와의 차가 가장 적은 값의 위치(idx)를 탐색
        idx = bisect.bisect(SUM_2, k-i) -1
        
        #이진탐색시 k와 정확히 일치하지 않는 경우, k보다 크지 않은 가장 작은 값을 탐색한다.
        #따라서 idx와 k보다 큰 값중 가장 가까운 idx+1번째 값을 비교하여 k에 더 가까운 값의 위치(idx)를 저장
        if abs(k- SUM_2[idx] - i) > abs(k- SUM_2[min(ls, idx+1)] - i):
            idx += 1
        
        #찾은 idx와 i를 더함(x). 현재 저장된 근사값(closest)과 비교하여 더 가까운 값을 closest에 저장
        x = i + SUM_2[idx]
        closest = sorted([closest, x], key=lambda x : (abs(k-x), x))[0]
        
    print(closest)
        