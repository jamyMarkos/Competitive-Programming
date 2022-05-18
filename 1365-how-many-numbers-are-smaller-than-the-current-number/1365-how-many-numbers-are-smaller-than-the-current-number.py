class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[i] > nums[j] and j != i:
                    cnt += 1
            arr.append(cnt)
        return arr