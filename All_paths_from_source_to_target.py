class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        Hash = defaultdict(list)
        n = len(graph)
        for i in range(n):
            Hash[i] = graph[i]
            
        start, final = 0, n - 1
        
        paths = []
        
        def dfs(cur, lst):
            nonlocal final
            if cur == final:
                paths.append(lst)
                return 
            for nxt in Hash[cur]:
                dfs(nxt, lst + [nxt])
                
        dfs(start, [0])
      
        return paths
        