class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        heard_news = set()
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append(i)

        def dfs(cur):
            heard_news.add(cur)
            if informTime[cur] == 0:
                return 0
            tt = float('-inf')
            for nbr in graph[cur]:
                if nbr not in heard_news:
                    tt = max(tt, dfs(nbr))
            return tt + informTime[cur]

        return dfs(headID)
     