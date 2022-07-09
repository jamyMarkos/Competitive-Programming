class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        m = []
        for i in range(len(r)):
            m.append([l[i],r[i]])
        def testArth(arr: list[int]) -> bool:
            test = True
            arr.sort()
            interval = arr[1] - arr[0]
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] == interval:
                    continue
                else:
                    test = False
                    break
            return test
       
        for i in m:
            ans.append(testArth(nums[i[0]:i[1]+1]))
        return ans
        
                