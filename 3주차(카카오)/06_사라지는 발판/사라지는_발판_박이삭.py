def solution(board, aloc, bloc):
    A_stack = [tuple(aloc)]
    B_stack = [tuple(bloc)]
    winner, steps = A_play(board, A_stack, B_stack, 0)
    print("A", 0, A_stack[-1], winner, steps)
    return steps


def A_play(board, A_stack, B_stack, step):
    res = {"A":[], "B":[]}
    ar, ac = A_stack[-1]

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr = ar + dr
        nc = ac + dc

        if nr not in range(len(board)) or nc not in range(len(board[0])):
            continue

        if board[nr][nc] and (nr, nc) not in A_stack and (nr, nc) not in B_stack[:-1]:
            if A_stack[-1] == B_stack[-1]:
                res["A"].append(step + 1)
            else:
                A_stack.append((nr, nc))
                winner, steps = B_play(board, A_stack, B_stack, step + 1)
                res[winner].append(steps)
                A_stack.pop()

    if res["A"]:
        return ("A", min(res["A"]))
    elif res["B"]:
        return ("B", max(res["B"]))
    else:
        return ("B", step)


def B_play(board, A_stack, B_stack, step):
    res = {"A":[], "B":[]}
    br, bc = B_stack[-1]

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr = br + dr
        nc = bc + dc

        if nr not in range(len(board)) or nc not in range(len(board[0])):
            continue

        if board[nr][nc] and (nr, nc) not in A_stack[:-1] and (nr, nc) not in B_stack:
            if A_stack[-1] == B_stack[-1]:
                res["B"].append(step + 1)
            else:
                B_stack.append((nr, nc))
                winner, steps = A_play(board, A_stack, B_stack, step + 1)
                res[winner].append(steps)
                B_stack.pop()

    if res["B"]:
        return ("B", min(res["B"]))
    elif res["A"]:
        return ("A", max(res["A"]))
    else:
        return ("A", step)


if __name__ == "__main__":
    board = ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 1, 1, 1, 1]], [[1]])
    aloc = ([1, 0], [1, 0], [0, 0], [0, 0])
    bloc = ([1, 2], [1, 2], [0, 4], [0, 0])
    for i in range(4):
        print(i, solution(board[i], aloc[i], bloc[i]))