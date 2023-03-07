class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(int)
        hash_map[0] = 1
        sum_ = 0
        count = 0

        for num in nums:
            sum_ += num
            if sum_ % k in hash_map:
                count += hash_map[sum_ % k]
            hash_map[sum_ % k] += 1
            # hash_map[num % k] += 1

        return count