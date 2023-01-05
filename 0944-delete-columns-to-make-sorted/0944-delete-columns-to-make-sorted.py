class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        arr = [[*str_] for str_ in strs]
        list_ = []
        for _ in arr:
            list_ += [_]
        zipper = list(zip(*list_))
        
        count = 0
        for column in zipper:
            for i in range(1, len(column)):
                if column[i-1] > column[i]:
                    count += 1
                    break
        return count
        
            
        
       
        
        