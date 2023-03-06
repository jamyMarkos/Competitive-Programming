class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        hash_ = defaultdict(int)

        for r in range(len(s)):
            hash_[s[r]] += 1
            max_count = max(list(hash_.values()))
            
            if (r - l + 1) - max_count <= k:
                max_len = max(r - l + 1, max_len)
            else:
                while (r - l + 1) - max_count > k:
                    hash_[s[l]] -= 1
                    max_count = max(list(hash_.values()))
                    l += 1
                max_len = max(r - l + 1, max_len)

        return max_len