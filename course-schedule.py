class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        order = []
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        q = deque()

        for i in range(numCourses):
            if not indeg[i]:
                q.append(i)

        while q:
             cur = q.popleft()
             order.append(cur)
             for nbr in graph[cur]:
                 indeg[nbr] -= 1
                 if indeg[nbr] == 0:
                     q.append(nbr)

        return False if len(order) != numCourses else True