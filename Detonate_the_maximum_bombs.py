class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        N = len(bombs)
        res = 0
        
        for i in range(N):
            for j in range(N):
                if i != j:
                    p = bombs[i][:-1]
                    q = bombs[j][:-1]
                    if bombs[i][-1] >= math.dist(p, q):
                        graph[i].append(j)
                        
        def dfs(vertex, visit):
            nonlocal res
            visit.add(vertex)
            res = max(res, len(visit))
            
            for nxt in graph[vertex]:
                if nxt not in visit:
                    dfs(nxt, visit)
                    
                    
        for node in range(N):
            dfs(node, set())
                        
        return res
        