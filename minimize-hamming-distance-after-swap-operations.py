class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        N = len(source)
        parent = {i:i for i in range(N)}
        rank = [1]*N

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rep_x, rep_y = find(x), find(y)
            if rank[rep_x] > rank[rep_y]:
                rep_x, rep_y = rep_y, rep_x
            parent[rep_y] = rep_x
            rank[rep_x] += rank[rep_y]

        for a, b in allowedSwaps:
            union(a, b)

        src = defaultdict(list)

        for i in range(N):
            src[find(i)].append(i)

        res = 0
        for lst in src.values():
            ss = defaultdict(int)
            tt = defaultdict(int)

            for i in lst:
                ss[source[i]] += 1
                tt[target[i]] += 1

            for n, count in ss.items():
                res += min(count, tt[n])

        return N - res