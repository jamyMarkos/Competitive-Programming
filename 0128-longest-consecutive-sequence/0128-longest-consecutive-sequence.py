class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for el in hashset:
            if el - 1 not in hashset:
                count = 1
                while (el + count) in hashset:
                    count += 1
                longest = max(count, longest)
                
        return longest
                
        