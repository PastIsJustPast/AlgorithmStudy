import sys


sys.stdin = open('../../../ArgorithmStudy/5주차(삼성)/4013_특이한자석/sample_input.txt')


def rot_magnet(num, rot_dir, prop_dir):
    if prop_dir:
        if 0 <= num + prop_dir < 4:
            if magnets[num][prop_dir * 2] != magnets[num + prop_dir][prop_dir * -2]:
                rot_magnet(num + prop_dir, rot_dir * -1, prop_dir)
    else:
        if num + 1 < 4:
            if magnets[num][2] != magnets[num + 1][-2]:
                rot_magnet(num + 1, rot_dir * -1, 1)
        if num - 1 >= 0:
            if magnets[num][-2] != magnets[num - 1][2]:
                rot_magnet(num - 1, rot_dir * -1, -1)
    magnets[num] = magnets[num][-rot_dir:] + magnets[num][:-rot_dir]


T = int(input())
for t in range(1, T+1):
    K = int(input())
    magnets = [[int(x) for x in input().split()] for _ in range(4)]
    for _ in range(K):
        magnet_num, direction = map(int, input().split())
        magnet_num -= 1
        rot_magnet(magnet_num, direction, 0)
    answer = 0
    for i, magnet in enumerate(magnets):
        answer += magnet[0] * (2 ** i)
    print(f'#{t} {answer}')
