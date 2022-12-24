class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_ = dict()
        for num in nums:
            if num in dict_:
                return True
            else:
                dict_[num] = 1
        return False