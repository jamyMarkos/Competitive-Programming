class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        i, j = 0, n-1
        while i < j:
            if height[i] < height[j]:
                temp = i
                h = height[i]
            else:
                temp = j
                h = height[j]
            ans = max(ans, (j-i) * h)
            if i + 1 == temp + 1:
                i += 1
            else:
                j -= 1
        return ans
                
                
            