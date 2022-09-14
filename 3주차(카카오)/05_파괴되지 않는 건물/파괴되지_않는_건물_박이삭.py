def solution(board, skill):
    answer = 0
    sum_table = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    for s in skill:
        accumulate_sum(sum_table, s)

    for r in range(len(board)):
        operand = 0
        for c in range(len(board[0])):
            operand += sum_table[r][c]
            sum_table[r][c] = operand

    for c in range(len(board[0])):
        operand = 0
        for r in range(len(board)):
            operand += sum_table[r][c]
            sum_table[r][c] = operand
            if board[r][c] + operand > 0:
                answer += 1

    return answer

def accumulate_sum(table, skill):
    t, r1, c1, r2, c2, degree = skill
    table[r1][c1] += [-degree, degree][t - 1]
    table[r2 + 1][c1] += [degree, -degree][t - 1]
    table[r1][c2 + 1] += [degree, -degree][t - 1]
    table[r2 + 1][c2 + 1] += [-degree, degree][t - 1]