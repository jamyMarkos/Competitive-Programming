class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if not n:
            return 1
        _len = len(bin(n)) - 2
        res = '1' * _len
        
        return int(res, 2) ^ n