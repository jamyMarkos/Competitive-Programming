class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ = 0
        
        left, right = 0, 1
        
        while right < len(prices):
            if prices[left] < prices[right]:
                tmp = prices[right] - prices[left]
                max_ = max(max_, tmp)
                
            elif prices[left] > prices[right]:
                left = right
                
            right += 1
            
        return max_
        