n, m, l, k = map(int, input().split())
starXY = [list(map(int, input().split())) for _ in range(k)]
bounce = 0 # 튕겨낸 별똥별 갯수
# 2중 for문 -> 별똥별을 튕겨낼 수 있는 위치
for i in range(0, k):
    for j in range(0, k):
        cnt = 0
        x = starXY[i][0]
        y = starXY[j][1]
        # 튕긴 별똥별 갯수
        for p in range(0, k):
            nx = starXY[p][0]
            ny = starXY[p][1]
            # 트램펄린 내부 -> 튕긴 횟수 더해주기
            if (x <= nx and x+l >= nx and y <= ny and y+l >= ny):
                cnt += 1
        bounce = max(bounce, cnt)
print(k-bounce) # 지구와 충돌된 별똥별 갯수
