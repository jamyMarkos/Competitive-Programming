class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for org, ngbrs in graph.items():
            if  len(graph[org]) >= 2:
                return org