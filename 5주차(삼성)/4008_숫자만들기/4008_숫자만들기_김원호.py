import sys


sys.stdin = open('../../../ArgorithmStudy/5주차(삼성)/4008_숫자만들기/sample_input.txt')


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a * b < 0:
        return -(abs(a) // abs(b))
    return a // b


def dfs(operators, nums, k, result):
    global max_val, min_val
    if k == len(nums):
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    for operator, cnt in enumerate(operators):
        if cnt:
            operate = OPERATOR_MAP[operator]
            operators[operator] -= 1
            new_result = operate(result, nums[k])
            dfs(operators, nums, k + 1, new_result)
            operators[operator] += 1


OPERATOR_MAP = {0: add,
                1: minus,
                2: multiply,
                3: divide}

T = int(input())
for t in range(1, T+1):
    N = int(input())
    operators = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    max_val = -100000000
    min_val = 100000000
    dfs(operators, nums, 1, nums[0])
    answer = max_val - min_val
    print(f'#{t} {answer}')