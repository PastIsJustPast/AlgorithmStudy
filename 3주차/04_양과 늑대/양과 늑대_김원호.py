class Node:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.children = []

    def __str__(self):
        return f'id : {self.id}, wovles : {self.wolves}\n'

    def __hash__(self):
        return self.id


def dfs(candidates, sheep_cnt, wolves_cnt):
    if wolves_cnt >= sheep_cnt:
        return sheep_cnt
    dfs_ret = []
    for candidate in candidates:
        new_candidates = candidates - set([candidate]) | set(candidate.children)
        ret = dfs(new_candidates, sheep_cnt + 1 - candidate.type, wolves_cnt + candidate.type)
        dfs_ret.append(ret)
    if dfs_ret:
        return max(dfs_ret)
    return sheep_cnt

def solution(info, edges):
    nodes = [Node(i, _type) for i, _type in enumerate(info)]
    for p, child in edges:
        nodes[child].p = nodes[p]
        nodes[p].children.append(nodes[child])

    return dfs(set(nodes[0].children), 1, 0)

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
answer = solution(info, edges)
print(answer)