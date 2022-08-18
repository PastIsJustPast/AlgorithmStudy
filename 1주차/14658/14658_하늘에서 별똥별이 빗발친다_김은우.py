#g3_q14658_하늘에서별똥별이빗발친다.py
'''
n: 맵 가로
m: 맵 세로
l: 트램펄린 가로, 세로
k: 별똥별 수

case#1. 지도를 생성하여 별을 저장하여 탐색하려 했으나, n, m 이 50만, 10만 이하이므로 메모리 초과 발생
case#2. 지도를 생성하지 않고 딕셔너리 형태로 저장하여 탐색하려 했으나 시간 초과
        n, m을 기준으로 탐색하려 하면 범위가 넓으므로 탐색이 어려움
        별은 최대 100개 이므로 별을 기준으로 탐색을 시도
case#3. 별이 모퉁이에 있는 경우로 탐색하려 했으나 그런 경우 ◇ 모양으로 배치되어 있는 경우 오답 발생
case#4. 그림을 그려보니 두 별의 행과 열이 만나는 지점을 모퉁이로 하는 경우가 최대값
'''
n, m, l, k = map(int, input().split())  
stars = [list(map(int, input().split())) for _ in range(k)]

MAX = 0

for i in range(k):
    for j in range(k):
        x = stars[i][0]
        y = stars[j][1]
        total = len([0 for a, b in stars if x <= a <= x+l and y <= b <= y+l])
        MAX = max(MAX, total)
        
print(k-MAX)