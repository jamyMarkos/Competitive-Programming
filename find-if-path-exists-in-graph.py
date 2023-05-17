class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        rank = [1] * n
        def union(x, y):
            p_x = find(x)
            p_y = find(y)

            if rank[p_x] >= rank[p_y]:
                parent[p_y] = p_x
                rank[p_x] += rank[p_y]
            else:
                parent[p_x] = p_y
                rank[p_y] += rank[p_x]

        def find(x):
            if parent[x] == x:
                return x
            rep = find(parent[x])
            parent[x] = rep
            return rep

        for a, b in edges:
            union(a, b)

        return find(source) == find(destination)