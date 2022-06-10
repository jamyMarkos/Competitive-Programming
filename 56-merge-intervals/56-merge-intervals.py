class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        list1 = []
        list1.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] <= list1[-1][1]:
                if intervals[i][1] < list1[-1][1]:
                    continue
                else:
                    list1[-1][1] = intervals[i][1]
            else:
                list1.append([intervals[i][0],intervals[i][1]])
        return list1
        
            
           
            
            
            
            
                
                
                
        
                
        