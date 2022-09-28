"""
구현 문제
class 사용했다가 시간 초과
재귀로 했다가 memory 초과
for loop으로 풀어서 통과
"""
REFLECT = reflect = {
            "u": ["u", "d", "r", "l", "d", "d"],
            "d": ["d", "r", "u", "u", "l", "u"],
            "l": ["l", "u", "d", "r", "r", "r"],
            "r": ["r", "l", "l", "d", "u", "l"],
        }
MOVES = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}


def start(r, c, dir):
    score = 0
    start_pos = (r, c)

    while True:
        dr, dc = MOVES[dir]
        next_pos = (r + dr, c + dc)

        if isend(*next_pos, start_pos):
            break

        if next_pos in WORMHOLES:
            r, c = WORMHOLES[next_pos]
        else:
            r, c = next_pos
            next_dirs = REFLECT[dir]
            ds = 1

            if isout(*next_pos, len(MAP_LIST)):
                dir = next_dirs[5]
            else:
                next_block = MAP_LIST[r][c]
                dir = next_dirs[next_block]
                ds = next_block > 0

            score += ds
        
    return score


def isout(r, c, size):
    return not (r in range(size) and c in range(size))


def isend(r, c, start):
    if not isout(r, c, len(MAP_LIST)):
        return MAP_LIST[r][c] == -1 or (r, c) == start
    else:
        return False

for T in range(int(input())):
    map_size = int(input())
    MAP_LIST = []
    STARTABLE = []
    WORMHOLES = {}
    HISTORY = {}
    for i in range(map_size):
        map_row = list(map(int, input().split()))
        for j, e in enumerate(map_row):
            if e == 0:
                STARTABLE.append((i,j))
            elif e in range(6, 11):
                if e not in WORMHOLES:
                    WORMHOLES[e] = (i, j)
                else:
                    wormhole = WORMHOLES[e]
                    WORMHOLES[wormhole] = (i, j)
                    WORMHOLES[(i, j)] = wormhole
        MAP_LIST.append(map_row)

    ans = 0
    for r, c in STARTABLE:
        for direction in MOVES.keys():
            ans = max(ans, start(r, c, direction))
    print(f"#{T+1}", ans)
