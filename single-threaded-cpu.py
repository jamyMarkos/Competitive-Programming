class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        H, A, ans = [], [], []
        i = 0
        for a, p in tasks:
            heappush(H, (a, i))
            i += 1

        time = H[0][0]
        
        count = 0
        while count < len(tasks):

            while H and H[0][0] <= time:
                arr, idx = heappop(H)
                heappush(A, (tasks[idx][1], idx))

            else:
                if A:
                    count += 1
                    pro_time, i = heappop(A)
                    ans.append(i)
                    time += pro_time
                else:
                    time = H[0][0]

        return ans