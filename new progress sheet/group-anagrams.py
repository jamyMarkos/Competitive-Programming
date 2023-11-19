class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dict_ = defaultdict(list)
        
        for str_ in strs:
            temp = ''.join(sorted(str_))
            dict_[temp].append(str_)
            
        return dict_.values()
        