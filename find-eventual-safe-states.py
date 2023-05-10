class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:   
        color = defaultdict(int)
        ans = []

        def dfs(node):
            if color[node] == 1:
                return False

            if color[node] == 2:
                return True

            color[node] = 1
            for nbr in graph[node]:
                if not dfs(nbr):
                    return False
            
            color[node] = 2
            ans.append(node)
            return True
        
        for i in range(len(graph)):
            if color[i] in [1, 2]:
                continue
            dfs(i)
        
        return sorted(ans)
                
        
                    

            
            
        
        
        return []