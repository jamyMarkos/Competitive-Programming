class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ans = [-1,-1]
        n = len(edges)
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if parent[x] == x:
                return x
            rep = find(parent[x])
            parent[x] = rep
            return rep

        def union(x, y):
            rep_x = find(x)
            rep_y = find(y)

            if rep_x != rep_y:
                if rank[rep_x] >= rank[rep_y]:
                    parent[rep_y] = rep_x
                    rank[rep_x] += rank[rep_y]
                else:
                    parent[rep_x] = rep_y
                    rank[rep_y] += rank[rep_x]
            else:
                ans[0], ans[1] = x+1, y+1

        for a, b in edges:
            union(a-1, b-1)

        return ans