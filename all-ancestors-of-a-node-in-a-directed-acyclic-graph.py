class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [set() for _ in range(n)]
        indeg = [0] * (n)
        graph = defaultdict(list)
        q = deque()

        for a, b in edges:
            graph[a].append(b)
            indeg[b] += 1

        for i in range(n):
            if not indeg[i]:
                q.append(i)

        while q:
            cur = q.popleft()
            for nbr in graph[cur]:
                res[nbr].add(cur)
                for el in res[cur]:
                    res[nbr].add(el)
                indeg[nbr] -= 1
                if not indeg[nbr]:
                    q.append(nbr)

        return [sorted(lst) for lst in res]