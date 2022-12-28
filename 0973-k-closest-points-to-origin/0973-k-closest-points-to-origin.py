class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        ans = []
        
        for list_ in points:
            dist = sqrt(list_[0] ** 2 + list_[1] ** 2)
            arr.append(dist)
            
        llist = list(zip(points, arr))
        final = sorted(llist, key = lambda x: [x[1]])
        
        for i in range(k):
            ans.append(final[i][0])
        return ans
            