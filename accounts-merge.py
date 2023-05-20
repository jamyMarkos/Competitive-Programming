class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = {i: i for i in range(n)}

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
            for j in range(i+1, n):
                if len(set(accounts[i]).intersection(accounts[j])) > 1:
                    union(i, j)
        
        ans = defaultdict(list)
        for i in range(n):
            ans[find(i)].append(i)

        final_ans = []
        for key, lst in ans.items():
            tmp = set()
            name = accounts[key][0]
            for idx in lst:
                tmp.update(set(accounts[idx][1:]))
            tmp = sorted(list(tmp))
            tmp.insert(0, name)
            final_ans.append(tmp)

        return final_ans