import sys

sys.stdin = open('../../../ArgorithmStudy/5주차(삼성)/4014_활주로건설/sample_input.txt')


def is_possible(line, X):
    prev = line[0]
    cnt = 0
    for num in line:
        if num == prev:
            cnt += 1
        else:
            if prev == num + 1:
                if cnt < 0:
                    return False
                cnt = -X + 1
            elif prev == num - 1:
                if cnt < X:
                    return False
                cnt = 1
            else:
                return False
            prev = num
    return cnt >= 0


T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    board = []
    for _ in range(N):
        board.append([int(x) for x in input().split()])
    answer = 0
    for line in board:
        answer += is_possible(line, X)
    for line in zip(*board):
        answer += is_possible(line, X)
    print(f'#{t} {answer}')
