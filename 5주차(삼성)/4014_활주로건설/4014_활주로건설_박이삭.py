def available(line, X):
    temp = line[0]
    placed = -1
    for pos, height in enumerate(line):
        if height != temp:
            if (
                height - temp == 1
                and placed < pos - X
                and line[pos - X : pos] == (temp,) * X
            ):
                temp = height
                continue
            elif height - temp == -1 and line[pos : pos + X] == (height,) * X:
                placed = pos + X - 1
                temp = height
                continue
            else:
                return 0

    else:
        return 1


T = int(input())

for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    top_map = [tuple(int(height) for height in input().split()) for _ in range(N)]
    num_lane = 0

    for row in top_map:
        num_lane += available(row, X)

    for column in zip(*top_map):
        num_lane += available(column, X)

    print(f"#{test_case} {num_lane}")
