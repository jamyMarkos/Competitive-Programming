class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parents = {i:i for i in range(n)}
        rank = {i:1 for i in range(n)}

        def find(x):
            if parents[x] == x:
                return x
            rep = find(parents[x])
            parents[x] = rep
            return rep

        def union(x, y):
            parents[find(x)] = find(y)
        
        for a, b in pairs:
            union(a, b)

        hashT = defaultdict(list)
        for i in range(n):
            hashT[find(i)].append(i)

        res = ['']*n
        for key, lst in hashT.items():
            tmp = sorted([s[i] for i in lst])

            for idx, val in enumerate(sorted(lst)):
                res[val] = tmp[idx]

        return ''.join(res)