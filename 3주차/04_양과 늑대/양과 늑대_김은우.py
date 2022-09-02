def solution(info, edges):
    global MAX
    MAX = 0
    def dfs(togo, sheep_n, wolf_n):
        global MAX
        if sheep_n <= wolf_n or not togo:
            MAX = max(MAX, sheep_n)
            return
        
        for idx, i in enumerate(togo):
            dfs(togo[:idx] + togo[idx+1:] + ch[i], sheep_n+(info[i]+1)%2, wolf_n+info[i]%2)

    ch = [[] for _ in range(len(info))]
    
    for parent, child in edges:
        ch[parent].append(child)
    
    dfs(ch[0], 1, 0)
    
    return MAX