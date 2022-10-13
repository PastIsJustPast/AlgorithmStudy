"""
비활성화 상태에서 활성화, 활성화 상태에서 죽음 상태로의 전환을 순서에 맞게 처리해주는 문제.
처음 세포의 상태는 비활성화, 활성화 이후 첫 스텝에서만 복제 진행.
"""


def duplicate(activate, deactivate, dead):
    # 새로 태어난 세포를 저장할 dictionary 선언
    new_cells = {}

    # 활성세포들 처리
    for position, state in list(activate.items()):
        # 첫 스텝 시 복제 진행
        if state[0] == state[1]:
            r, c = position
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                npos = (r + dr, c + dc)
                # 자리가 비어있으면 복제 진행
                if not (npos in deactivate or npos in activate or npos in dead):
                    # 자리에 세초가 없거나 생존 시간이 더 큰 경우 업데이트
                    if npos not in new_cells or state[0] > new_cells[npos][0]:
                        new_cells[npos] = [state[0], state[0]]

        # 생존 가능 시간 차감
        state[1] -= 1

        # 생존 가능 시간 모두 소모 시
        if not state[1]:
            del activate[position]
            dead.add(position)

    # 비활성세포 처리
    for position, state in list(deactivate.items()):
        # 잠복기 차감
        state[1] -= 1

        # 잠복기 모두 지나면 활성화
        if not state[1]:
            activate[position] = [state[0], state[0]]
            del deactivate[position]

    # 새로 복제된 세포들 비활성화 세포로 업데이트
    deactivate.update(new_cells)


T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    activate = {}
    deactivate = {}
    dead = set()

    for r in range(N):
        for c, cell in enumerate(map(int, input().split())):
            if cell:
                deactivate[(r, c)] = [cell, cell]

    for _ in range(K):
        duplicate(activate, deactivate, dead)

    print(f"#{test_case} {len(activate) + len(deactivate)}")
