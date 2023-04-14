class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        colors = {}
        graph = defaultdict(list)
        
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
            
        def color_vertices(vertex):
            for neighbor in graph[vertex]:
                if neighbor in colors:
                    if colors[neighbor] == colors[vertex]:
                        return False
                else:
                    colors[neighbor] = 3 - colors[vertex]
                    if not color_vertices(neighbor):
                        return False
            return True
     
        
        for vertex in graph:
            if vertex not in colors:
                colors[vertex] = 1
                if not color_vertices(vertex):
                    return False
                
        return True