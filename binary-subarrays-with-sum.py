class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hash_ = defaultdict(int)
        hash_[0] = 1
        count, sum_ = 0, 0

        for num in nums:
            sum_ += num
            if sum_ - goal in hash_:
                count += hash_[sum_ - goal]
            hash_[sum_] += 1

        return count