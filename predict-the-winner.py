class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
    
        def predictor(start,end,turn): 
            if start == end:
                if turn:
                    return [nums[start],0]
                else:
                    return [0, nums[start]]
                
            if turn: 
                score = predictor(start+1, end, False)
                score[0] += nums[start]
                score2= predictor(start, end-1, False)
                score2[0] += nums[end]
                
                if score[0] >= score2[0]:
                    return score
                return score2
               
            else: 
                score = predictor(start+1, end, True)
                score[1] += nums[start]
                score2= predictor(start, end-1, True)
                score2[1] += nums[end]
                
                if score[1] >= score2[1]:
                    return score
                return score2
        
        ans = predictor(0, len(nums)-1, True)
        return ans[0] >= ans[1]