import sys


sys.stdin = open('../../../ArgorithmStudy/5주차(삼성)/2117_홈방법서비스/sample_input.txt')


def get_dist(service, house):
    return abs(service[0] - house[0]) + abs(service[1] - house[1])


def get_under_service_house(size, houses):
    cost = size ** 2 + (size - 1) ** 2
    max_house_cnt = 0
    for i in range(N):
        for j in range(N):
            house_cnt = 0
            for house in houses:
                if get_dist((i, j), house) < size:
                    house_cnt += 1
            if house_cnt * M >= cost:
                max_house_cnt = max(max_house_cnt, house_cnt)
    return max_house_cnt


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    houses = []
    for i in range(N):
        line = map(int, input().split())
        for j, num in enumerate(line):
            if num:
                houses.append((i, j))
    for service_size in range(2 * N, 0, -1):
        answer = get_under_service_house(service_size, houses)
        if answer:
            break
    print(f'#{t} {answer}')
