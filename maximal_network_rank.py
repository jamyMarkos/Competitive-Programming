class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        max_net_rank = 0
        
        graph = defaultdict(list)
        
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
            
        for i in range(n):
            for j in range(i+1, n):
                
                tt = len(graph[i]) + len(graph[j]) # - len(graph[i].intersection(graph[j]))
                if i in graph[j]:
                    tt -= 1
                max_net_rank = max(max_net_rank, tt)
                    
        return max_net_rank
                    
            
        