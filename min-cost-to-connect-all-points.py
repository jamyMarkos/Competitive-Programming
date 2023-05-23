class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adjList = {i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adjList[i].append([dist, j]) 
                adjList[j].append([dist, i]) 
        
        res = 0
        minH = [[0, 0]]
        visit = set()

        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for nbrCost, nbr in adjList[i]:
                if nbr not in visit:
                    heapq.heappush(minH, [nbrCost, nbr])

        return res