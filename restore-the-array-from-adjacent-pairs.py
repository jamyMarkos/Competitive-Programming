class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        ans = []
        visit = set()
        
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        stack = []
        for key, lst in graph.items():
            if len(lst) == 1:
                if key not in visit:
                    stack.append(key)
                    visit.add(key)
                while stack:
                    cur = stack.pop()
                    
                    ans.append(cur)
                    for nbr in graph[cur]:
                        if nbr not in visit:
                            stack.append(nbr)
                            visit.add(nbr)
                # break

        return ans