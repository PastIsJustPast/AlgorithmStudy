# 효율성 못품
from dataclasses import dataclass


@dataclass
class Skill:
    id: int
    skill_type: int
    r1: int
    c1: int
    r2: int
    c2: int
    __degree: int

    @property
    def degree(self):
        if self.skill_type == 1:
            return -self.__degree
        return self.__degree

    def __str__(self):
        return f'[r1: {self.r1}, c1: {self.c1}, r2: {self.r2}, c2: {self.c2}]'

    def __eq__(self, other):
        if isinstance(other, Skill):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __add__(self, other):
        assert isinstance(other, Skill), 'adding different class'
        return self.degree + other.degree


def binary_search(arr, n, attr, func):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        abc = getattr(arr[mid], attr)
        if func(getattr(arr[mid], attr), n):
            start = mid + 1
        else:
            end = mid - 1
    return start


def is_a_lte_b(a, b):
    return a <= b


def is_a_lt_b(a, b):
    return a < b


def solution(board, skill):
    skills = [Skill(id, *_skill) for id, _skill in enumerate(skill)]
    skills_r1_order = [*skills]
    skills_c1_order = [*skills]
    skills_r2_order = [*skills]
    skills_c2_order = [*skills]
    skills_r1_order.sort(key=lambda x: x.r1)
    skills_c1_order.sort(key=lambda x: x.c1)
    skills_r2_order.sort(key=lambda x: x.r2)
    skills_c2_order.sort(key=lambda x: x.c2)

    N = len(board)
    M = len(board[0])
    x2r_slice_set = {}
    y2c_slice_set = {}
    px = {}
    py = {}
    influential_skills = {}
    influent_degree = {}
    for k in range(N * M):
        x, y = divmod(k, M)
        if x not in x2r_slice_set:
            r1_idx = binary_search(skills_r1_order, x, 'r1', is_a_lte_b)
            r1_slice = skills_r1_order[:r1_idx]
            r2_idx = binary_search(skills_r2_order, x, 'r2', is_a_lt_b)
            r2_slice = skills_r2_order[r2_idx:]
            x2r_slice_set[x] = set(r1_slice) & set(r2_slice)
        if y not in y2c_slice_set:
            c1_idx = binary_search(skills_c1_order, y, 'c1', is_a_lte_b)
            c1_slice = skills_c1_order[:c1_idx]
            c2_idx = binary_search(skills_c2_order, y, 'c2', is_a_lt_b)
            c2_slice = skills_c2_order[c2_idx:]
            y2c_slice_set[y] = set(c1_slice) & set(c2_slice)
        r_slice_set = x2r_slice_set[x]
        c_slice_set = y2c_slice_set[y]
        px[0] = 0
        py[0] = 0
        if x not in px:
            if x2r_slice_set[x] == x2r_slice_set[x - 1]:
                if x - 1 in px:
                    px[x] = px[x - 1]
                else:
                    px[x] = x - 1
            else:
                px[x] = x
        if y not in py:
            if y2c_slice_set[y] == y2c_slice_set[y - 1]:
                if y - 1 in py:
                    py[y] = py[y - 1]
                else:
                    py[y] = y - 1
            else:
                py[y] = y
        if px[x] not in influential_skills:
            influential_skills[px[x]] = {}
        if py[y] not in influential_skills[px[x]]:
            influential_skills[px[x]][py[y]] = r_slice_set & c_slice_set
        if px[x] not in influent_degree:
            influent_degree[px[x]] = {}
        if py[y] not in influent_degree[px[x]]:
            prev_x, prev_y = divmod(k - 1, M)
            if y:
                influent_degree[px[x]][py[y]] = sum(map(lambda _skill: _skill.degree,
                                                        influential_skills[px[x]][py[y]] -
                                                        influential_skills[px[prev_x]][py[prev_y]])) - \
                                                sum(map(lambda _skill: _skill.degree,
                                                        influential_skills[px[prev_x]][py[prev_y]] -
                                                        influential_skills[px[x]][py[y]])) + \
                                                influent_degree[px[prev_x]][py[prev_y]]
            else:
                influent_degree[px[x]][py[y]] = sum(map(lambda _skill: _skill.degree, influential_skills[px[x]][py[y]]))
        board[x][y] += influent_degree[px[x]][py[y]]
    answer = 0
    for row in board:
        answer += len(list(filter(lambda x: x > 0, row)))
    return answer


board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]

answer = solution(board, skill)
print(answer)
