from collections import deque

queue = deque()
R, C = map(int, input().split())

maps = [input() for _ in range(R)]
queue.append((0, 0))
moves = 1
visit = set()
visit.add((0, 0))

# BFS
while queue:
    for _ in range(len(queue)):
        r, c = queue.popleft()

        for mr, mc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = r + mr
            nc = c + mc
            if nr == R - 1 and nc == C - 1:
                queue = None
                break
            if nr in range(R) and nc in range(C):
                if (nr, nc) not in visit and maps[nr][nc] == "1":
                    visit.add((nr, nc))
                    queue.append((nr, nc))

        if queue is None:
            break

    moves += 1

print(moves)
