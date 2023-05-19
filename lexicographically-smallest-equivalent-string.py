class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        parent = {chr(i+97): chr(i+97) for i in range(26)}

        def find(x):
            if parent[x] == x:
                return x
            rep = find(parent[x])
            parent[x] = rep
            return rep

        def union(x, y):
            rep_x = find(x)
            rep_y = find(y)

            if rep_x > rep_y:
                rep_x, rep_y = rep_y, rep_x
            parent[rep_y] = rep_x
            

        for i in range(n):
            union(s1[i], s2[i])

        res = []

        for ch in baseStr:
            res.append(find(ch))

        return ''.join(res)