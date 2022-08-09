'''
##
문제 유형 : BF

##
풀이법
1.최초에는 2차원 리스트 완전 탐색으로 품 -> 시간초과
2.각 별들의 위치를 트램펄린 좌상단으로 간주 -> 시간초과 + 오답
3.별들이 모서리에 올 수 있도록 별의 좌표를 조합해서 탐색 -> 시간초과
4. 3번과 유사하나 트램펄린 위치 받고 별이 트램펄린에 들어오는지 탐색  품

##쟁점
- 50만 x 50만이라 시간을 고려해야 함

##어려운 점
- 2차원 리스트 완전탐색을 사용하지 않고 트램펄린이 별똥별을 최대한 많이 튕구는 상황을 찾는게 어려움
 -> 별 좌표의 조합 사용

##시간 복잡도
100 * 100 * 100

'''


from copy import deepcopy
n,m,l,k = map(int,input().split()) #별똥별 구역의 가로길이, 세로길이, L은 트램펄린의 한변 길이, k는 별동뼐 수
stars =[]
xs,ys = set(), set()
for _ in range(k):
    x,y = map(lambda x : int(x) - 1 , input().split())
    stars.append((x,y))
    xs |= set([x])
    ys |= set([y])


max_cnt = 0
#별 모서리 위치
for x in xs:
    for y in ys :
        cnt = 0
        #if ((x + l) >= n) or ((y + l) >= m) : continue #애초에 초과되면 넘기기

        #각 별이 트램펄린 안에 있는지 확인
        for sx,sy in stars :
            if x <= sx <= x + l and y <= sy <= y + l : #별이 트램펄린 안에 있다면
                 cnt += 1
        max_cnt = max(max_cnt , cnt)

print(k - max_cnt)

