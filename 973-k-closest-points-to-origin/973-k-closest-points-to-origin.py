class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def func(arr):
            return math.sqrt((arr[0] ** 2) + (arr[1] ** 2))
        for i in range(len(points)):
            points[i].append(func(points[i]))
            
        arr1 = sorted(points, key=lambda x: x[2])
        arr2 = []
        i = 0
        while i < k:
            arr2.append(arr1[i][:-1])
            i += 1
        return arr2
        
            
            
            
                    
        