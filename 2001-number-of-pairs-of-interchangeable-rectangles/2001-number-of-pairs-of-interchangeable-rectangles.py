class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count_ = 0
        hash_ = {}
        
        for rect in rectangles:
            ratio = rect[0] / rect[1]
            
            if ratio in hash_:
                count_ += hash_[ratio]
                hash_[ratio] += 1
            else:
                hash_[ratio] = 1  
                
        return count_
                
        