# 처음 문제접근법
# N,M,L의 제한이 아주 컸다
# L*L의 격자로 모든 칸을 탐색하는것은 시간초과라고 생각하고 효율적인 방법을 생각하였다
# K의 갯수가 작은것에 포인트를 잡고 각 별들을 중심으로 북동 북서 남동 남서 방향으로 다른 별들이 몇개있는지 체크하였다 ( 자신은 가장 모서리에 있다는 가정이다
# 왜냐면 최대로 많이 별을 팅기게 하기위해 현자 자신의 별은 모서리에 있고 L만큼의 범위를 4가지 방면으로 탐색해보기 위해서였다 )
# 틀렸다고 나온다 => 무엇이 틀린지는 모르겠으나 문제의 의도를 제대로 파악하지 못하였다


# import sys
#
# si = sys.stdin.readline
#
# M, N, L, K = map(int , si().split())
#
# stars = []
#
# for _ in range(K):
#
#     x,y = map(int, si().split())
#
#     if y == N and x == M:continue
#     if y == 1 and x == M:continue
#     if y == N and x == 1:continue
#     if y == 1 and x == 1:continue
#
#     stars.append((y,x))
#
# # 4개의 면을 확인해보기 위해 북동 , 북서, 남동 , 남서 방향으로 지정한다
#
# dir = [(-1, 1),(-1, -1),(1, 1),(1, -1)]
# dump_stars = 0
# for i in range(K-1):
#     cy, cx = stars[i]
#     for k in range(4):
#         cnt = 1 # 별 자신을 선택한다
#         ny, nx = cy + (dir[k][0] * (L-1)), cx + (dir[k][1] * (L-1))
#         for j in range(K-1):
#             if i == j: continue
#             ey, ex = stars[j]
#             if ny < cy and nx > cx:
#                 if ny <= ey < cy and cx < ex <= nx:
#                     cnt += 1
#             elif nx < cx and ny > cy:
#                 if cy < ey <= ny and nx <= ex < cx:
#                     cnt += 1
#             elif ny < cy and nx < cx:
#                 if ny <= ey < cy and nx <= ex < cx:
#                     cnt += 1
#             else:
#                 if cy < ey <= ny and cx < ex <= nx:
#                     cnt += 1
#         dump_stars = max(dump_stars, cnt)
# size = len(stars)
# print(size - dump_stars)


####################################################################################s


# 완전탐색은 시간초과 버리고
# 그러면 k시간으로 세제곱을 해도 시간안에 들수 있습니다. ( 관찰 : 아이디어 )
# 트램펄린에 튕겨저 나갈 별의 갯수를 구할 함수 생성
# n,m,l,k 입력받음
# 별의 위치를 입력받음
# 별중 2개를 고른 후 , 그 별이 트램펄린에서 이웃한 모서리에  걸쳐지게 트램펄린이 위치하게  한 후 계산한다
# 이 연산을 k^2 즉 모든 별들끼리 모서리에 위치했을 경우 범위안에 드는 별들의 수를 구한 후 뺍니다.
# x의 변위와 y의 변위 사이의 별들의 갯수가 최대가 되었을 경우 떨어지는 별들을 최소화할 수 있다
# 비슷한문제 : 고기잡이 ( 7573 )
import sys

si = sys.stdin.readline

n, m, l, k = map(int, si().split())

stars = []

answer = 0

for _ in range(k):
    x,y = map(int, si().split())
    stars.append((x,y))

def gogo(x,y):
    global answer
    cnt = 0
    for i in range(k):
        if x <= stars[i][0] <= x + l and \
            y <= stars[i][1] <= y + l:
                cnt += 1
        answer = max(answer,cnt)

for i in range(k):
    for j in range(k):
        #
        gogo(stars[i][0],stars[j][1])


print(k-answer)



