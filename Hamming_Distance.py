class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x^y
        
        bitCount=0

        while ans > 0:
            bitCount+=ans&1
            ans=ans>>1

        return bitCount
         