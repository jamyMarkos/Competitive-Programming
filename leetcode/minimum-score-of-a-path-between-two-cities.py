class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))

        def dfs(i):
            nonlocal res
            if i in visit:
                return
            visit.add(i)
            for nbr, dist in adj[i]:
                res = min(dist, res)
                dfs(nbr)

        res = float('inf')
        visit = set()
        dfs(1)
        return res
        