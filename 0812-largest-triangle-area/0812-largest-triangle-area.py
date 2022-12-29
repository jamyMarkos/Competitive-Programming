class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_, n = 0, len(points)
        
        def findArea(pt1, pt2, pt3) -> float:
            temp = 0.5 * ( abs(pt1[0] * (pt2[1] - pt3[1]) + pt2[0] * (pt3[1] - pt1[1]) + pt3[0] * (pt1[1] - pt2[1])))
            return temp
            
            
        
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    area_ = findArea(points[i], points[j], points[k])
                    max_ = max(area_, max_)
                    
        return max_
                    
                    
                    
        