import sys

sys.stdin = open('sample_input.txt')


def get_man_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_accessible_BC_idxes(pos):
    x, y = pos
    accessible_BC_idxes = set()
    for i, BC in enumerate(BCs):
        bc_x, bc_y, c, _ = BC
        if get_man_dist((x, y), (bc_x, bc_y)) <= c:
            accessible_BC_idxes.add(i)
    return accessible_BC_idxes


def choose_BC(BC_idxes):
    max_p = 0
    max_idx = -1
    for BC_idx in BC_idxes:
        _, _, _, p = BCs[BC_idx]
        if p > max_p:
            max_p = p
            max_idx = BC_idx
    return max_idx, max_p


dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]
T = int(input())
for t in range(1, T + 1):
    M, A = map(int, input().split())
    a_moves = [0] + [int(x) for x in input().split()]
    b_moves = [0] + [int(x) for x in input().split()]

    answer = 0
    BCs = []
    for _ in range(A):
        BCs.append([int(x) for x in input().split()])
    a = (1, 1)
    b = (10, 10)
    for a_move, b_move in zip(a_moves, b_moves):
        a = (a[0] + dx[a_move], a[1] + dy[a_move])
        b = (b[0] + dx[b_move], b[1] + dy[b_move])
        a_BC = get_accessible_BC_idxes(a)
        b_BC = get_accessible_BC_idxes(b)
        idx, p1 = choose_BC(a_BC)
        _, p2 = choose_BC(b_BC - set([idx]))
        idx, p3 = choose_BC(b_BC)
        _, p4 = choose_BC(a_BC - set([idx]))
        answer += max(p1 + p2, p3 + p4)
    print(f'#{t} {answer}')