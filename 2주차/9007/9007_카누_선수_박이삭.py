"""
Pypy3
메모리 419692KB
시간 4172ms

각 반들을 합한 모든 경우를 고려하면 O(n^4)으로 시간초과
잘 안떠올라서 질문 검색을 보니 두 반씩 합쳐서 사용하라고 했음..! O(n^2)

그렇게 앞선 두 반의 합과 뒤진 두 반의 합을 구하고 목표 k에 근접한 값을 구하기 위해 탐색을 한다.
둘 중 하나를 기준으로 원소를 뽑아 k와 차를 구하고 차에 근접한 원소를 이진탐색으로 찾는다.

시간을 줄이려고 여러번 수정했다. python3는 결국 안됨..

시간 복잡도
학생 몸무게 두 반씩 더하기 O(n^2)
정렬 O(log(n))
결과 탐색하기 O(n^2log(n))

Dominant term은 O(n^2log(n))
"""
import sys
from bisect import bisect_right

input = sys.stdin.readline

for case in range(int(input())):
    k, n = map(int, input().split())

    classes = [list(map(int, input().split())) for _ in range(4)]
    first = set()
    two = set()

    for i in range(n):
        for j in range(n):
            first.add(classes[0][i] + classes[1][j])
            two.add(classes[2][i] + classes[3][j])

    second = sorted(two)

    diff = (4e7, 8e7)

    for f in first:
        right = bisect_right(second, k - f)

        if second[right - 1] + f == k:
            diff = (0, k)
            break

        for s in second[max(0, right - 1):right + 1]:
            temp_diff = (abs(f + s - k), f + s)
            if diff > temp_diff:
                diff = temp_diff

    print(diff[1])