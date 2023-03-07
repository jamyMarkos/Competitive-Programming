class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=[0]
        rem={}
        count=0
        for i in nums:
            prefix.append(prefix[-1]+i)
        for i in prefix:
            if i%k in rem:
                count+=rem[i%k]
                rem[i%k]+=1
            else:
                rem[i%k]=1
        return count