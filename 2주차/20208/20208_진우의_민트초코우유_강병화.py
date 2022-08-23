# 2차원 격자
# 관찰 N의 크기가 10 이하 => 완탐 가능성이 높다
# 최대로 마실 수 있는 민트초코우유 갯수
# 이동하다가 체력소진하면 더이상 이동불가 다시 다른길로 이동해서 민트초코우유를 먹을 수 있는지 확인
# 브루트포스에서도 백트래킹으로 풀기
# 집에서 출발
# 집으로 돌아오는경우는 집의 좌표를 찍게 되면 오키 못찍고 체력이 0이되면 다른길 다시 탐색
# 완전탐색
# import sys
#
# si = sys.stdin.readline
# N,M,H = map(int, si().split())
# town = [list(map(int, si().split())) for _ in range(N)]
# # 우선 집의 위치를 알아야한다
# answer = 0
# def backtracking(homey,homex,cury,curx,M,count):
#     global answer
#     if M < 0:
#         return
#     if homey == cury and homex == curx: # 집에 도착하면 최댓값을 갱신한다
#         answer = max(answer, count)
#         return
#     for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
#         ny = cury + dy
#         nx = curx + dx
#         if ny < 0 or ny >= N or nx < 0 or nx >= N: continue # 범위를 벗어나면 이동하지 않는다
#         if town[ny][nx] == 2:
#             # 그 다음 칸에 초코우유가 있을 경우 체력을 회복하면서 기존체력 1의 소모값을 뺀다 , 초코우유 갯수는 +1 이다
#             backtracking(homey, homex, ny, nx, M - 1 + H, count + 1)
#         elif town[ny][nx] == 0:
#             # 그 다음 칸에 초코우유가 없을 경우 체력소모만 일어난다
#             backtracking(homey, homex, ny, nx, M - 1, count)
#
#
# for i in range(N):
#     for j in range(N):
#         # 진우의 집을 발견하면 바로 백트래킹 완탐 시작
#         if town[i][j] == 1:
#             hy,hx = i,j
#             # 남쪽으로 갔을 경우 최대 마실수있는 초코우유 갯수
#             for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 ny = hy + dy
#                 nx = hx + dx
#                 if ny < 0 or ny >= N or nx < 0 or nx >= N: continue  # 범위를 벗어나면 이동하지 않는다
#                 if town[ny][nx] == 2:
#                     # 그 다음 칸에 초코우유가 있을 경우 체력을 회복하면서 기존체력 1의 소모값을 뺀다 , 초코우유 갯수는 +1 이다
#                     backtracking(hy, hx, ny, nx, M - 1 + H, 1)
#                 elif town[ny][nx] == 0:
#                     # 그 다음 칸에 초코우유가 없을 경우 체력소모만 일어난다
#                     backtracking(hy, hx, ny, nx, M - 1, 0)
# print(answer)
# 위의 풀이방법이 잘못된것은 아니지만 시간초과다 다음부터는 시간과 풀이방법을 완벽하게 구상한뒤에 코드에 손을 대는 습관을 들여야겠다
# 시간복잡도는 10!
# python3 : 시간초과
# pypy3 : 1764ms  메모리 : 120MB ( 브랜칭 적용 안함 )
# python3 : 840ms 메모리 : 30MB ( 브랜칭 적용시 )
import sys
si = sys.stdin.readline
N, M, H = map(int, si().split())
town = [list(map(int, si().split())) for _ in range(N)] # 마을 2차원 격자를 입력받는다
milks = [] # 우유들의 위치를 저장할 리스트를 생성한다
home_y, home_x = 0,0 # 집의 좌표를 담을 변수를 선언한다
answer = 0  # 최소는 0개로 설정한다
def dfs(cy, cx, hp, cnt):
    global answer
    # 끝까지 한번의 깊이를 들어가서 탐색했다면 끝난후 집까지의 거리를 계산해서 또 맨허튼 거리를 집까지 계산하여 집까지 도착할 수 있으면 최대 마신 우유 갯수를 업데이트한다
    # 현재 먹은 우유위치에서 집까지 도달할 수 있다면 최댓값 업데이트를 한다
    if abs(cy-home_y) + abs(cx-home_x) <= hp:
        answer = max(answer,cnt)
    # 브랜칭으로 현저히 시간을 줄인다
    if answer == total_milk:
        return
    # 순열 형태의 백트래킹 완전탐색이다 => 즉 순서가 있는 나열방법이다 우유를 어느것부터 마시느냐가 정답에 영향을 줄 수 있다
    for my,mx in milks:
        if town[my][mx] == 2: # 아직 우유를 마시지 않았다면 .
            distance = abs(cy-my) + abs(cx-mx)
            if distance <= hp: # 맨허튼 거리로 계산한 값이 현재체력으로 이동할 수 있다면
                town[my][mx] = 0 # 우유를 먹었다는 표시를 해주고 그 다음 우유를 먹으러 갑니다 즉 깊이 우선 탐색합니다.
                dfs(my, mx, hp-distance+H, cnt + 1)
                town[my][mx] = 2
for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            home_y, home_x = i , j
        elif town[i][j] == 2:
            milks.append((i,j))
total_milk = len(milks)
dfs(home_y, home_x, M, 0)
print(answer)